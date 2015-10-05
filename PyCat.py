import sys
import shutil

def main():
    if len(sys.argv) > 1:
        File_Name = sys.argv[1]
    else:
        print("What would you like to view?")
        File_Name = input("> ")
        if File_Name[-4] != ".txt":
            File_Name = File_Name + ".txt"


    read_File(File_Name)

    close()


def read_File(File_Name):
    f = open(File_Name, 'r')
    for i in f:
        print(i)

def close():
    input("Any key to exit!")
    sys.exit()
