from os import walk
from os import path
filenames = 0

def userInput():
    global file_location
    file_location = input('Directory to file :')
    if path.exists(file_location):
        print("File path {}".format(file_location))
    else:
        print("File location {} is not found".format(file_location) )
        file_location = input('Directory to searche file :')
    f = []
    for (dirpath, dirnames, filenames) in walk(file_location):
        f.extend(filenames)
        print(*f, sep = "\n")
        break

if __name__ == '__main__':
    userInput()
