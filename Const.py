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
    sleepSecond=300

    #取得ファイルの保存先
    dst_dir =r"D:\Users\temp"



