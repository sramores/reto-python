import os, glob

user = os.getlogin()
path = r'/home/' + user + '/Descargas/'
directory = os.listdir(path)

for file in directory:
    print(file)
