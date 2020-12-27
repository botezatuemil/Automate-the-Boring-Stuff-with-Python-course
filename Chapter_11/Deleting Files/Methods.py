import os, shutil, send2trash

# os.unlink(x) delete file
# os.rmdir(x) remove empty directory!!!
# shutil.rmtree(x) delete folder with content!!! no recycle bin!!

for file in os.listdir('c:\\Emil'):
    if file.endswith('.txt'):
        send2trash.send2trash(os.path.join('c:\\Emil', file))
        print(file)

# send2trash.send2trash('c:\\Emil\\brr.txt')