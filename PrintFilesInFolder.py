import os
import os.path
from os import path
import shutil
from datetime import datetime
host_name = 0
file_location = 0

#file_location = "C:/Users/vadim.a/Desktop"
#file_name = "download.jpg"

def main():
    # Print all items from the file
    for item in a:
        print(item)

def find_file(path, file_name):
    listfiles = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(file_name):
                path = os.path.join(root, file)
                print(os.path.join(root, file))
                listfiles.append(path)
    return listfiles


def userInput():
    global host_name
    global fili_location
    host_name = input('Host name :')
    if host_name[:-4] != 'http':
        print("Wrong host name")
        return
    file_location = input('Directory to file :')
    if path.exists(file_location):
        print("File path {}".format(file_location))
    else:
        print("File location {} is not found".format(file_location) )
        file_location = input('Directory to searche file :')

if __name__ == '__main__':
    userInput()
    a = find_file(file_location,host_name)
    main()
