# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 15:20:49 2019

@author: oddoy
"""

import json
data = json.load(open("data.json"))
type(data)

def translate(word):
    return data[word]

word = input("Enter word: ")

print(translate(word))
    
    