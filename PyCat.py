# A python implementation of the CAT Tool used in Linux
# This can be massively improved+

import sys
import shutil

def main():
    if len(sys.argv) > 1:
        # if the tool is called with an argument
        # use that argument as the file name
        #TODO CAT should be able to be used with more than 1 argument
        File_Name = sys.argv[1]
    else:
        print("What would you like to view?")
        File_Name = input("> ")
        # asks the user for a file to view
        if File_Name[-4] != ".txt":
            # if file does not end with .txt , add .txt to file
            File_Name = File_Name + ".txt"


    read_File(File_Name)

    close()


def read_File(File_Name):
    f = open(File_Name, 'r')
    # opens and recurseively prints every line of file
    for i in f:
        print(i)
    f.close()

def close():
    input("Any key to exit!")
    # waits for user to press any key to exit
    sys.exit()
