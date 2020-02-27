# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 18:13:10 2020

@author: werty
"""
import sys
T = int(input())

for i in range(0,T):
    A, B = map(int, input().split())
    A = A + 1
    N = int(input())
    
    guess = (A + B) // 2
    print(guess)
    sys.stdout.flush()
    guessed_in_loop = False
    for j in range(0,N-1):
        answer = input()
        if answer == 'CORRECT':
            #print("I guessed, leaving inner loop")
            guessed_in_loop = True
            break
        elif answer == 'TOO_SMALL':
            A = guess + 1
        elif answer == 'TOO_BIG':
            B = guess - 1
        elif answer == 'WRONG_ANSWER':
            break
        guess = (A + B) // 2
        #print('guess nr {}'.format(j+2))
        print(guess)
        sys.stdout.flush()
    if(guessed_in_loop == False):
        #read expected CORRECT input
        nil = input()
#print('Thats all folks')
