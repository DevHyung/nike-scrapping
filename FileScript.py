import os
import shutil
if __name__=="__main__":
    dirname = './'
    fileList = os.listdir(dirname)
    for filename in fileList:
        full_filename = os.path.join(dirname, filename)
        ext = os.path.splitext(full_filename)[-1]
        if ext.lower() == '.jpg' or ext == '.png':
            try:
                if '(바탕)' in filename:
                    shutil.copyfile(dirname + filename, dirname + filename.split('(바탕)')[0] + '/' + filename)
                else: #품번만 있는경우
                    folderName = ''
                    pureName = filename.split('.')[0][:10]
                    for tmp in fileList:
                        if pureName in tmp:
                            if not filename == tmp and not '.jpg' in tmp:
                                folderName = tmp
                                break
                    print(dirname + filename, dirname + folderName + '/' + filename)
                    shutil.copyfile(dirname + filename, dirname + folderName + '/' + filename)
            except:
                print("확인필요 >>> ", filename)
    print(">>> 파일 이동완료 !!!")
    input("아무키나누르시면 종료됩니다.")
    #shutil.move('./샘플파일/846886-222.JPG', './샘플파일/나이키 SB 아이콘 후디 846886-222/')
