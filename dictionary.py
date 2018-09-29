#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 13:07:34 2018

@author: niel99
"""
import json
from difflib import get_close_matches

data= json.load(open("data.json"))

def translate(w):
    if w in data.keys():
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn=input("Did you mean %s ?(Y for yes N for no)\n"%get_close_matches(w,data.keys())[0])
        if yn=="Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="N":
            return "Sorry no matches found for your word"
        else:
            return "Please press the correct keyword"
    else:
        return "Word doesn't exist Please try again"

word=input("Enter a word:")

l= translate(word)

if type(l)==list:
    for i in l:
        print(i)
else:
    print(l)