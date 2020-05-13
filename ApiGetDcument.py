import requests
import json

class GetDocument:

    def __init__(self,version,date,type) :
        self.version = version
        self.date = date
        self.type =type
        self.res_text =None
        self.yuho = []

    def GetEdinetList(self):
    
        url = "https://disclosure.edinet-fsa.go.jp/api/%s/documents.json" %self.version

        # 書類一覧APIのリクエストパラメータ
        params = {
        "date" : self.date,
        "type" : self.type
        }

        # 書類一覧APIの呼び出し
        res = requests.get(url, params=params, verify=False)

        # レスポンス（JSON）の表示
        #print(res.text)
        self.res_text = json.loads(res.text)

    def GetSearchList(self,wordSerch):
        count=0
        count2=0
        self.res_text["results"]

        for result in self.res_text["results"]:
            count +=1
            if result['docDescription'] is not None:
                if wordSerch in result['docDescription']:
                    print(result['docID'],result['docDescription'],result['filerName'])
                    self.yuho.append(result)
                    count2 +=1
        print(count,count2) 

        
    def GetNewYuho(self,kessan_day,doctype_code):
        count=0
        count2=0
        self.res_text["results"]

        for result in self.res_text["results"]:
            count +=1
            #if result['results']['docDescription'] is not None:
            if result['docDescription'] is not None :
                if result['docTypeCode'] == doctype_code and result['periodEnd'] == kessan_day :
                    print(result['docID'],result['docDescription'],result['filerName'],result['periodEnd'])
                    self.yuho.append(result)
                    count2 +=1
        print(count,count2)       
        return count2
        
    