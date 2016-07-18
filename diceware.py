'''
Created on Apr 25, 2014

@author: Kevin
'''

import random, string 

Words = map(string.strip, file("words.txt","rU").readlines()) 

def genPwd(): 
    Password = None 
    for N in [1,2,3]: 
        NewWord = random.choice(Words) 

        if None == Password: 
            Password = NewWord 
        else: 
            Password = Password + " " + NewWord 
    return Password 

for N in range(1,21): 
    print "%d. %s" % (N, genPwd()) 