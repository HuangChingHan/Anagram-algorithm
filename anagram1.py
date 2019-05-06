# -*- coding: utf-8 -*-
"""
Created on Mon May  6 22:15:47 2019

Topic : anagram method1
"""

def anagramCheck(string1, string2):
    if len(string1) != len(string2):
        label = False
    else:
        label = True
    
    alist = list(string2)
    pos1 = 0
    while label and pos1 < len(string1):
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if string1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        if found:
            alist[pos2] = None     
        else:
            label = False
        pos1 = pos1 + 1
    
    return label

print(anagramCheck('cbi','cih'))

