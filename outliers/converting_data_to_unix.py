# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 11:25:17 2021

@author: Dell
"""

original = "practice_outliers_ages.pkl"
destination = "practice_outliers_ages_unix.pkl"
 
content = ''
outsize = 0
with open(original, 'rb') as infile:
    content = infile.read()
with open(destination, 'wb') as output:
    for line in content.splitlines():
        outsize += len(line) + 1
        output.write(line + str.encode('\n'))
 
print("Done. Saved %s bytes." % (len(content)-outsize))