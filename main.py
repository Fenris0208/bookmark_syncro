#!/usr/bin/python3

import sys
import json


# Import der Klassen
import bookmark_class
import inputfile_class

def main(argv):
    print("parameter are :",argv) 

    # read inputfile


    # save bookmarks in database

    # check if bookmark exist



    # generate new bookmarkfile



    b1 = bookmark_class.bookmark("studium","www.blabla.de","16032021","studiumsscheiß")
    b1.get_contet()
    print(b1.generate_string())
   

def settings():
    print("settings under constructions")
'''
def load_file(): 

def load_bookmark():

def  
'''

if __name__=="__main__":
    main(sys.argv[1:])


