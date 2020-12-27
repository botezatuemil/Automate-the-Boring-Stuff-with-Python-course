import os

print(os.path.join('folder 1', 'folder 2', 'folder 3', 'folder 4'))
print(os.getcwd()) # show the directory I am working
print(os.path.abspath('os.py')) # show the absolute file path
print(os.path.isabs(r'..\\..\\os.png')) # is relative file path
print(os.path.isabs(r'c:\\os.png')) # is relative file path
print(os.path.getsize('os.py')) # show the size of the file
print(os.listdir(r'c:\Emil\Proiecte\Python\Proiecte Python\Automate the boring stuff')) # list all content
print(os.makedirs('c:desktop\\name')) # make directory

# 12A3c5!, 324d?G!

# we work in os.py so
# ..\\name skip to the previous folder
# ..\\..\\name skip to the last 2 folders before the file we are working
# join take every folder and concatenate to the file path,
# every file so we have the complete path we each folder that doesn't have a name

size = 0
for file in os.listdir(r'..\\Filenames and Absolute Filepaths'):
    if not os.path.isfile(os.path.join(r'..\\Filenames and Absolute Filepaths', file)):
        continue
    else:
        size += os.path.getsize(os.path.join(r'..\\Filenames and Absolute Filepaths', file))

print(size)
