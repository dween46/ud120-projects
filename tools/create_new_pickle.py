# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 23:46:02 2021

@author: Dell
"""

#!/usr/bin/env python
"""
convert dos linefeeds (crlf) to unix (lf)
usage: dos2unix.py 
"""
original = "../tools/word_data.pkl"
destination = "../tools/word_data_unix.pkl"
 
content = ''
outsize = 0
with open(original, 'rb') as infile:
    content = infile.read()
with open(destination, 'wb') as output:
    for line in content.splitlines():
        outsize += len(line) + 1
        output.write(line + str.encode('\n'))
 
print("Done. Saved %s bytes." % (len(content)-outsize))