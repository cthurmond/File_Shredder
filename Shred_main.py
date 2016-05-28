# I'm just messing around learning vim.
# I figure it's finally time for me to learn.

import sys

def main():
    if len(sys.argv) < 2:    
        print ("Usage: file_shredder.py <filename>")
    else:
        for i in range(1, len(sys.argv)):
            try:
                shred(sys.argv[i])
            except:
                print ("!!!!! ERROR !!!!!")

def shred(filename):
    print ("Shredding" + " " +  filename)

main()
