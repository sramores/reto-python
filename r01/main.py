import os

user = os.getlogin()
path = '/home/' + user + '/Descargas'

print(os.listdir(path))