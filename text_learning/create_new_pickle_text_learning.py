# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 14:18:55 2021

@author: Dell
"""
original = "your_email_authors.pkl" 
destination ="your_email_authors_unix.pkl" 
 
content = ''
outsize = 0
with open(original, 'rb') as infile:
    content = infile.read()
with open(destination, 'wb') as output:
    for line in content.splitlines():
        outsize += len(line) + 1
        output.write(line + str.encode('\n'))
 
print("Done. Saved %s bytes." % (len(content)-outsize))