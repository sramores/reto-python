import os
import imghdr

arrow = "=>"
printline = ""
counter = 0

def filechecker(path, file):
    if os.path.isfile(path + file) and imghdr.what(path + file) == 'jpeg':
        printline = ""
        
        counter += 1
        printline += str(counter) + " "
        
        if counter % 2 == 0:
            printline += arrow + " "
        
        # if file.title()
        #     file.capitalize()
        
        printline += file
        #counter = counter + 1
        print(printline)  

def main():
    cmd = "xdg-user-dir DOWNLOAD"

    path = "/home/sergio/Downloads/" #os.popen(cmd).read().strip() + "/"
    directory = os.listdir(path)

    print("Directorio: " + path + "\n") 
    
    for file in directory:
        filechecker(path, file) 
    
if __name__ == "__main__":
    main()
