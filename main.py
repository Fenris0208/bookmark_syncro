#!/usr/bin/python3

import sys
import json


# Import der Klassen
import bookmark_class
import inputfile_class

def main(argv):
    print("parameter are :",argv) 

    b1 = bookmark_class.bookmark("www.test.de","16.02.2021","studium")
    b1.get_contet()
   


'''
def load_file(): 

def load_bookmark():

def  
'''

if __name__=="__main__":
    main(sys.argv[1:])


