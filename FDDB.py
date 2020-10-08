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
    path_evaluate = 'FDDB.exe'
    a = 'D:/dataset/face/FDDB/FDDB-folds/FDDB-fold-ellipseList-all.txt'
    if pred == None:
        d = './FDDB-result/result.txt'
    else:
        d = pred
    f = '0'
    i = 'D:\\dataset\\face\\FDDB\\originalPics\\'
    l = 'D:/dataset/face/FDDB/FDDB-folds/FDDB-fold-all.txt'
    if result_path == None:
        r = './FDDB-result/'
    else:
        r = result_path
    z = '.jpg'
    s = index
    doPath = path_evaluate+' -a '+a+' -d '+d+' -f '+f+' -i '+i+' -l '+l+' -r '+r+' -z '+z+' -s '+str(s)
    print(doPath)
    system(doPath)

def genResultTxt(detector, RGB=True, output='./result.txt'):
    '''
    detector : the method to predict an unknown image.
    RGB : which datatype is the input data of detector, if True, than RGB, if False, than BGR.
    output : the output result located.

    Note that
        The method will be use with `detector(img)`, and output with list of [x1, y1, x2, y2, score],
        if your method is not look like that, you must transform with an outer function.
    '''
    maxScore = 0
    minScore = 0
    writeTxt = ''
    for count, path in enumerate(source_data):
        # get path & img
        print(count, path, end='')
        img = cv2.imread(self.__source_path + path + '.jpg')
        if RGB:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # detection
        bboxes = detector(img)

        # fprint to file
        temp = temp + '\n' + str(len(bboxes))
        for bbox in bboxes:
            rect = list(map(int, bbox[0:4]))
            w = rect[2] - rect[0]
            h = rect[3] - rect[1]
            temp = temp + '\n{} {} {} {} {}'.format(rect[0], rect[1], w, h, bbox[4])
            if (bbox[4] > maxScore):
                maxScore = bbox[4]
            elif (bbox[4] < minScore):
                minScore = bbox[4]
        writeTxt = writeTxt + temp + '\n'
    print(maxScore)
    print(minScore)
    with open (output, 'w') as fp:
        fp.write(writeTxt)

if __name__ == '__main__':
    '''
    call by -- $ python FDDB.py [detection] [result path]
    '''
    runFDDB(pred=sys.argv[1], result_path=sys.argv[2])
