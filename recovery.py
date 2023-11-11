from os import listdir, mkdir
from os.path import isfile, isdir, join
from shutil import copy
# ---- functions ----
def input_dirname(originalname):
    while True:
        name = input("new name> ")
        if name == "help":
            for f in listdir(originalname):
                dirsign = ""
                if isdir(join(originalname, f)):
                    dirsign = "(フォルダ)"
                print(f"   |- {[f]} {dirsign}")
            continue
        return name

def input_filename(originalname):
    while True:
        name = input("new name> ")
        if name == "help":
            with open(originalname, "r") as f:
                print(s for s in f.readlines(5))
            continue
        return name

def verifyDir(path, dirname):
    global rename_counter
    try:
        print(f"checking {path}/{dirname} ...OK")
    except:
        print(f"checking {path}/{[dirname]} ...要修正")
        rename_counter += 1
        newname = input_dirname(join(path, dirname))
        copy(join(path, dirname),join(path, newname))
        dirname = newname
    
    path = join(path, dirname)
    print(f"    --{dirname}フォルダの中身を確認します")
    for f in listdir(path):
        verify(path, f)

def verifyFile(path, filename):
    global rename_counter
    try:
        print(f"checking {path}/{filename} ...OK")
    except:
        print(f"checking {path}/{[filename]} ...要修正")
        rename_counter += 1
        newname = input_filename(join(path, filename))
        copy(join(path, filename),join(path, newname))
        filename = newname

def verify(path, filename):
    if isfile(join(path, filename)):
        verifyFile(path, filename)
    else:
        verifyDir(path, filename)
# ---- end ----
# ---- main ----
rename_counter = 0
pathname = "/home/pi/Documents/01_生徒用" #/home/pi/Documents/01_生徒用
print(
    """メモ
01_生徒用フォルダを復元します。
復元が終わり次第、USBディスクに保存し、ラズパイ11番は初期化してください。
01_生徒用フォルダのリネームだけは手動で行う必要があります。行なわれていない場合「01_生徒用　フォルダの存在確認」がエラーになるのでご連絡ください。
-- 動ける環境かどうかチェックします。"""
)

print("\n\n01_生徒用　フォルダの存在確認", end="")
if len(listdir(pathname)) == 0:
    print(f"\n{pathname}　が見つからないか空のようです。空の場合、フォルダを削除してください。その他の場合、中川にご連絡ください。")
    exit()
else:
    print("  ... OK")


print("\n\n復元作業を開始します")
print("途中で文字化けしたフォルダ、ファイルの名前を聞かれることがあります。勘などで決めてください。helpと入力すると概要が見れます。")
print("ファイルを表示するソフトを起動してください。起動したらstartと打ってください。")
while input("> ") != "start":
    print("ファイルを表示するソフトを起動してください。起動したらstartと打ってください。")

for f in listdir(pathname):
    verify(pathname, f)

print("一通りの整理が終了しました。終了ならq,最終チェックならcを入力")
while True:
    command = input("command> ")
    if command == "q":
        exit()
    elif command == "c":
        rename_counter = 0
        for f in listdir(pathname):
            verify(pathname, f)
        if rename_counter == 0:
            print("フォルダは全て復元されました。マネージャーに報告のもと、USBディスクに移動してください。ラズパイ11番は初期化してください。")
            exit()
        else:
            print("一通りの整理が終了しました。終了ならq,最終チェックならcを入力")