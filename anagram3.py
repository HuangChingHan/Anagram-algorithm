# -*- coding: utf-8 -*-
"""
Created on Mon May  6 23:37:28 2019

Topic : anagram method3
"""

def anagramCheck(string1, string2):
    if len(string1) != len(string2):
        label = False
    else:
        label = True
    
    c1 = [0]*26
    c2 = [0]*26
    
    for i in range(len(string1)):
        pos = ord(string1[i]) - ord('a')
        c1[pos] = c1[pos] + 1 

    for i in range(len(string2)):
        pos = ord(string2[i]) - ord('a')
        c2[pos] = c2[pos] + 1
    
    j = 0
    while j < 26 and label:
        if c1[j] == c2[j]:    
            j = j + 1
        else:
            label = False
    
    
    return label
print(anagramCheck('assq','fgre'))
