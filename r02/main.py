import os
import imghdr

cmd = "xdg-user-dir DOWNLOAD"

path = os.popen(cmd).read().strip() + "/"
directory = os.listdir(path)

print("Directorio: " + path + "\n")

def filechecker(path, file):
    if os.path.isfile(path + file) and imghdr.what(path + file) == 'jpeg':
        print(file)

for file in directory:
    filechecker(path, file)

