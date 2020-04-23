#https://non-dimension.com/get-xbrldata/
import requests
import datetime
import json
import sys
import zipfile
from pathlib import Path
import shutil
import os
from Const import ConstClass
import time
import ApiGetDcument

# def GetEdinetList(version,date,type):

#   url = "https://disclosure.edinet-fsa.go.jp/api/%s/documents.json" %version

#   # 書類一覧APIのリクエストパラメータ
#   params = {
#     "date" : date,
#     "type" : type
#   }

#   # 書類一覧APIの呼び出し
#   res = requests.get(url, params=params, verify=False)

#   # レスポンス（JSON）の表示
#   #print(res.text)
#   res_text = json.loads(res.text)

#   return res_text

# def GetSearchList(results,wordSerch):
#   yuho = []
#   count=0
#   count2=0
#   results= results["results"]

#   for result in results:
#     count +=1
#     #if result['results']['docDescription'] is not None:
#     if result['docDescription'] is not None:
#       if wordSerch in result['docDescription']:
#         print(result['docID'],result['docDescription'],result['filerName'])
#         yuho.append(result)
#         count2 +=1
#   print(count,count2)        
#   return yuho

def GetCompanyDocument(documentList,version,type):
  count = 0
  for list in documentList:
    docid = list["docID"]  
    count +=1
    url = "https://disclosure.edinet-fsa.go.jp/api/%s/documents/" %version + docid 
    
    params = {
      "type":type
    }
    if type == ConstClass.document_type2:
      filename =  docid + ".pdf"
    else :
      filename =  docid + ".zip"

    #dst_dir =r"D:\Users\jumpei-iwano\temp"
    res = requests.get(url,params=params,verify=False)

    if res.status_code==200:
      try:
        with open(filename,'wb') as f:
          for chunk in res.iter_content(chunk_size=1024):
            f.write(chunk)

        if type !=ConstClass.document_type2:
          with zipfile.ZipFile(filename) as existing_zip:
            existing_zip.extractall(docid)
          shutil.move(os.path.join(os.getcwd(), filename), ConstClass.dst_dir)
          shutil.move(os.path.join(os.getcwd(), docid), ConstClass.dst_dir)
        else :
          shutil.move(os.path.join(os.getcwd(), filename), ConstClass.dst_dir)
          shutil.move(os.path.join(os.getcwd(), docid), ConstClass.dst_dir)

      except :
        pass
  print(count)

#メインで実行されたときのみ動作する。
if __name__ == '__main__':

  #本日の日付を取得
  Date = datetime.date.today()

  #初期値設定
  boolean = True
  count = 0
  totalcount = 0

  #取得したいドキュメントリスト
  searchDocument = int(input("取得したいドキュメントリストを指定してください。（例）1：提出本文書、2：PDF、3：添付資料、4：英文　:"))


  #検索Word
  searchWord = input("指定したい検索ワードがあれば入力してください。（例）有価証券報告書：　")

  #確認用
  # temp = ApiGetDcument.GetDocument(ConstClass.VERSION,Date,ConstClass.List_type2)
  # temp.GetEdinetList()
  # print(temp.res_text)

  while boolean:

    res_text1 = ApiGetDcument.GetDocument(ConstClass.VERSION,Date,ConstClass.List_type1)
    res_text1.GetEdinetList()
    
    if count !=int(res_text1.res_text["metadata"]["resultset"]["count"]):
      res_text2 = ApiGetDcument.GetDocument(ConstClass.VERSION,Date,ConstClass.List_type2)
      res_text2.GetEdinetList()
      res_text2.GetSearchList(searchWord)
      GetCompanyDocument(res_text2.yuho,ConstClass.VERSION,searchDocument)
    
    time.sleep(ConstClass.sleepSecond)
    totalcount +=1
    count = res_text1.res_text["metadata"]["resultset"]["count"]

    #一定時間ループしたら終了
    if totalcount == 12:
      boolean = False
else:
  print("本モジュールからメイン実行してください。")

def FileCompress():
  pass

