#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import codecs

def replace_line(line):
    newstr = u''
    replace_str = line[0] != "<"
    line = line.decode('utf-8')
    for s in line:
        if s == "<":
            replace_str = False
        if s == ">":
            replace_str = True
        if not replace_str:
            newstr += s
        else:
            if s.lower() == "s":
                newstr += u"$"
            elif s.lower() == "c":
                newstr += u'¢'
            else:
                newstr += s
    return newstr

# Script should be called from the xml/ directory
files = os.listdir(os.getcwd())
files = [f for f in files if f.endswith('.xml')]

for file in files:
    print(file)
    with open(file, 'r') as fh:
        lines = fh.readlines()

    with codecs.open(file, 'w', 'utf-8') as fh:
        for line in lines:
            newline = replace_line(line)
            fh.write(newline)
