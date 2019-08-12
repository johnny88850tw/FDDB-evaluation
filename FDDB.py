import sys
from os import system

def runFDDB(pred=None, result_path=None, index=-1):
    # 設定evaluate參數
    # -a : ground truth的TXT檔
    # -d : 你的演算法產生的答案TXT檔
    # -f : 0 使用矩形，1 使用橢圓，2 使用點陣列
    # -i : 放置照片的目錄 (originalPics)
    # -l : 記錄所有圖片的TXT檔
    # -r : 將要存放ROC輸出的目錄
    # -z : 使用".jpg"
    # -s : 搜尋需要輸出的圖片
    path_evaluate = './FDDB.exe'
    a = './FDDB/FDDB-folds/FDDB-fold-ellipseList-all.txt'
    if pred == None:
        d = './FDDB-result/result.txt'
    else:
        d = pred
    f = '0'
    i = '.\\FDDB\\originalPics\\'
    l = './FDDB/FDDB-folds/FDDB-fold-all.txt'
    if result_path == None:
        r = './FDDB-result/'
    else:
        r = result_path
    z = '.jpg'
    s = index
    doPath = path_evaluate+' -a '+a+' -d '+d+' -f '+f+' -i '+i+' -l '+l+' -r '+r+' -z '+z+' -s '+str(s)
    print(doPath)
    system(doPath)

if __name__ == '__main__':
    '''
    call by -- $ python FDDB.py [detection] [result path]
    '''
    runFDDB(pred=sys.argv[1], result_path=sys.argv[2])