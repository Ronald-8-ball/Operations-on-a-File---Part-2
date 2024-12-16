file = open('Hacking.txt','x')
file.close()
import os
os.remove('file2.txt')
os.rmdir('Folder1')