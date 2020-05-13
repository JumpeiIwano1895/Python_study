#https://non-dimension.com/get-xbrldata/
import requests
import datetime
import json
import sys
import os
from Const import ConstClass
import time
import ApiGetDcument

#gotlist_docId.append(result['docID'])

class GetNewDocumentClass:
  gotlist_docid = []

def Notification(documentList,version):

  for list in documentList:
    docid = list["docID"]  
    url = "https://disclosure.edinet-fsa.go.jp/api/%s/documents/" %version + docid + "?type=1"
    filerName = list["filerName"] 
    docDescription = list["docDescription"] 
    submitDateTime = list["submitDateTime"] 

    if docid not in GetNewDocumentClass.gotlist_docid:
      res = requests.post(
        ConstClass.webhook_url,
        json={
          "text": "\n\n" + submitDateTime +"\n【要確認】Edinetに最新版タクソノミで記述した有価証券報告書がUPされました。\n対象は下記URLをご確認ください。\n\n"+ filerName +"\n" +docDescription +"\n" + url + "\n",
          "thread":{
          "name":webhook_res
          }
        }
      )
      GetNewDocumentClass.gotlist_docid.append(docid)

#メインで実行されたときのみ動作する。
if __name__ == '__main__':

  #本日の日付を取得
  Date = datetime.date.today()

  #初期値設定
  boolean = True
  count = 0
  totalcount = 0
  target = True
  args = sys.argv
  
  #取得したいドキュメントリスト
  # searchDocument = int(input("取得したいドキュメントリストを指定してください。（例）1：提出本文書、2：PDF、3：添付資料、4：英文　:"))
  #searchDocument =1

  #検索Word
  # searchWord = input("指定したい検索ワードがあれば入力してください。（例）有価証券報告書：　")
  #searchWord = "有価証券報告書"
  #searchWord = args[1]

  # kessan = input("決算日を指定してください。（例）20220-03-31：　")
  #kessan_day = "2020-02-19"
  kessan_day = args[1]

  res = requests.post(
    ConstClass.webhook_url,
    json={"text": str(Date) + "　本日の処理を開始します。\n※18時30分頃まで1時間おきに3月31日決算の有価証券報告書が無いか検索します。\n"}
  )

  webhook_res = json.loads(res.text)["thread"]["name"]

  while boolean:

    #インスタンス作成
    res_text1 = ApiGetDcument.GetDocument(ConstClass.VERSION,Date,ConstClass.List_type1)
    res_text1.GetEdinetList()
    
    if count !=int(res_text1.res_text["metadata"]["resultset"]["count"]):
      res_text2 = ApiGetDcument.GetDocument(ConstClass.VERSION,Date,ConstClass.List_type2)
      res_text2.GetEdinetList()
      result = res_text2.GetNewYuho(kessan_day,ConstClass.doctype_code_yuho)
      if result > 0:
        Notification(res_text2.yuho,ConstClass.VERSION)
        target = False

    totalcount +=1
    count = res_text1.res_text["metadata"]["resultset"]["count"]
    time.sleep(ConstClass.sleepSecond)

    #一定時間ループしたら終了
    if totalcount == ConstClass.total_get_count:
      boolean = False
      if target:
        response = requests.post(
          ConstClass.webhook_url,
          json={
            "text": "\n"+ str(Date) +"　本日、該当資料はありませんでした。\n 本日の処理を終了します。",
            "thread":{
              "name":webhook_res
            }
          }
        )
      else:
        response = requests.post(
          ConstClass.webhook_url,
          json={
            "text": "\n" + str(Date) +" 本日の処理を終了します。",
            "thread":{
                "name":webhook_res
            }
          }
        )
else:
  print("本モジュールからメイン実行してください。")

def FileCompress():
  pass

