import os

cmd = "xdg-user-dir DOWNLOAD"

path = os.popen(cmd).read().strip()
directory = os.listdir(path)

print("Directorio: " + path + "\n")

for file in directory:
    if os.path.isfile(path + "/" + file):
        print(file)
