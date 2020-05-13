class ConstClass:
    #定数
    VERSION = "v1"

    #書類一覧APIの取得タイプ
    #メタデータのみ
    List_type1 =1

    #提出書類一覧とメタデータ
    List_type2 =2

    #書類取得APIの取得タイプ
    document_type1 = 1
    document_type2 = 2
    document_type3 = 3
    document_type4 = 4
    
    #何分おきにファイルを取得するか。5分（300秒）
    #sleepSecond=3600
    sleepSecond=3600

    #計何回ファイル取得を実行するか（回数）
    total_get_count=9

    #取得ファイルの保存先
    dst_dir =r"D:\Users\temp"
    
    #書類種別コード 有価証券報告書=120
    doctype_code_yuho ="120"

    #Gogleチャットの通知先URL
    webhook_url = 'https://chat.googleapis.com/v1/spaces/AAAAxU-Wv3Q/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=zgeUxpi9X9OncZIRYVMxDBlJyuIUyRLDpCMU-Zm7qz4%3D'



