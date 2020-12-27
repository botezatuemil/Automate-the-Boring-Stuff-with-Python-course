import os, shutil

for foldername, subfolders, filenames in os.walk('c:\\Emil\\Cursuri'):
    print('The folder is ' + foldername)
    print('The subfolders in ' + foldername + ' are:' + str(subfolders))
    print('The filenames in ' + foldername + ' are:' + str(filenames))
    print()

    for subfolder in subfolders:
        if 'fish' in subfolder:
            os.rmdir(subfolder)

    for file in filenames:
        if file.endswith('.py'):
            shutil.copy(os.join(foldername, file), os.join(foldername, file + '.backup'))


