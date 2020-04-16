import requests
import datetime
import json
import sys
import zipfile
from pathlib import Path
import shutil
import os

args = sys.argv

print("EDINETのバージョンを入力してください。 例：バージョン1の場合⇒v1 ",end='')
#VERSION = input()
VERSION = "v1"

# 書類一覧APIのエンドポイント
url = "https://disclosure.edinet-fsa.go.jp/api/%s/documents.json" %VERSION

Date =  datetime.date.today()

# 書類一覧APIのリクエストパラメータ
params = {
  "date" : Date,
  "type" : 2
}



# 書類一覧APIの呼び出し
res = requests.get(url, params=params, verify=False)

# レスポンス（JSON）の表示
#print(res.text)

res_text = json.loads(res.text)

#res_text内のresultsの内容を取得
results= res_text["results"]

#resultsの中身（docID, docDescription, filerName）を表示
# for result in results:
#   print(result['docID'],result['docDescription'],result['filerName'])

kessan = []
sihanki = "有価証券"
count=0

for result in results:
  count +=1
  if result['docDescription'] is not None:
    if sihanki in result['docDescription']:
      print(result['docID'],result['docDescription'],result['filerName'])
      kessan.append(result)
print("ループ回数は%i" %count)

i=0
for list in kessan:
  
  docid = list["docID"]
  print(docid)

  url = "https://disclosure.edinet-fsa.go.jp/api/v1/documents/" + docid

  params = {
    "type":1
  }

  #filename = 'D:\Users\jumpei-iwano\work\' + docid + '.zip'
  #filename = docid + '.zip'
  filename =  docid + ".zip"
  dst_dir =r"D:\Users\jumpei-iwano\temp"
  res = requests.get(url,params=params,verify=False)

  if res.status_code==200:
    with open(filename,'wb') as f:
      for chunk in res.iter_content(chunk_size=1024):
        f.write(chunk)

  with zipfile.ZipFile(filename) as existing_zip:
    existing_zip.extractall(docid)
  shutil.move(os.path.join(os.getcwd(), filename), dst_dir)
  filename =  docid
  shutil.move(os.path.join(os.getcwd(),filename), dst_dir)



