#!/usr/bin/python
from terminalFunctions import *
from terminal import *
import re

# https://www.codeeval.com/public_sc/108/



# Read the input file
input = open('input.txt', 'r')
# input = open('input1.txt', 'r')

# tokens
tokens = {
    '^c'     : 'clear',
    '^h'     : 'topLeft',
    '^b'     : 'startOfCurrentLine',
    '^d'     : 'oneRowDown',
    '^u'     : 'oneRowUp',
    '^l'     : 'oneColumnLeft',
    '^r'     : 'oneColumnRight',
    '^e'     : 'eraseCharacter',
    '^i'     : 'insertMode',
    '^o'     : 'overwriteMode',
    '^^'     : 'circumflex',
    }

# terminal
terminal = Terminal()

for line in input:
    splitter = re.compile(r'(\^[c,h,b,d,u,l,r,e,i,o,\^]|\^\d{2}|\W|s)')
    splits = re.split(splitter, line)
    splits = [x for x in splits if x != ''] # Remove the empty items created by the split
    splits.pop() # Remove the last element (new line coming from the reading of the file)

    print splits

    for s in splits:
        if s != '':
            if s in tokens:
                print s + "   " + tokens[s]
                locals()[tokens[s]](terminal).__str__()
            elif ( re.search(r'\^\d{2}', s) ):
                print s + "   changeCoordinates(" + s[1] + " " + s[2] + ")"
                changeCoordinates(terminal, int(float(s[1])), int(float(s[2])))
            else:
                for c in s:
                    if c != "\n":
                        print s + "   addChar(" + c + ")"
                        addChar(terminal, c)

            print ""
            print terminal.__str__()
            print ""
