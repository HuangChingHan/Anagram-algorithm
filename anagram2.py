# -*- coding: utf-8 -*-
"""
Created on Mon May  6 23:16:31 2019

Topic : anagram method2
"""

def anagramCheck(string1, string2):
    if len(string1) != len(string2):
        label = False
    else:
        label = True
        
    list1 = list(string1)
    list2 = list(string2)
    list1.sort()
    list2.sort()
    
    pos = 0
    while label and pos < len(string1):
        if list1[pos] == list2[pos]:
            pos = pos + 1
        else:
            label = False    
    
    
    return label

print(anagramCheck('adf','fad'))
