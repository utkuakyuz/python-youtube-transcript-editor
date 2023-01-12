# -*- coding: utf-8 -*-
"""
@author: Utku Akyüz
"""

a_file = open("text.txt", "r")
lines = a_file.readlines()
a_file.close()
count = 0
new_file = open("sample.txt", "w")
for line in lines:
    line = line.replace('\n', ' ').replace('\r', '')
    line.strip() 
    if line.strip("\n") != "line2":
        if count % 2 == 1:
            print(line);
            line = ""
        count += 1
        new_file.write(line)
        

new_file.close()