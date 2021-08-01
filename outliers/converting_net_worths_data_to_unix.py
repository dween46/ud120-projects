# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 01:22:13 2021

@author: Dell
"""


original = "practice_outliers_net_worths.pkl"
destination = "practice_outliers_net_worths_unix.pkl"
 
content = ''
outsize = 0
with open(original, 'rb') as infile:
    content = infile.read()
with open(destination, 'wb') as output:
    for line in content.splitlines():
        outsize += len(line) + 1
        output.write(line + str.encode('\n'))
 
print("Done. Saved %s bytes." % (len(content)-outsize))