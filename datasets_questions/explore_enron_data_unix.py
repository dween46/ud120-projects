# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 21:06:33 2021

@author: Dell
"""

original = "../final_project/final_project_dataset.pkl"
destination = "../final_project/final_project_dataset_unix.pkl"
 
content = ''
outsize = 0
with open(original, 'rb') as infile:
    content = infile.read()
with open(destination, 'wb') as output:
    for line in content.splitlines():
        outsize += len(line) + 1
        output.write(line + str.encode('\n'))
 
print("Done. Saved %s bytes." % (len(content)-outsize))