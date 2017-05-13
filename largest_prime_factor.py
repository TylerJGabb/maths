import sys
import math as M
import time as T
##What is the largest prime factor of a number n
##Prime numbers, if they are more than 1 digit, end in 
## 1,3,7,9
file = open('LPF.csv','w')

def isprime1(n):
    if n < 10: 
        #print('stage1')
        return n in (2,3,5,7)
    if int(str(n)[-1]) not in (1,3,7,9):
        #print('stage2')
        return False 
    top = M.floor(M.sqrt(n))
    #print('stage3')
    #print(top)
    for digit in range(2,top+1):
        if n%digit == 0: return False
    return True
 

#Trying to find a pattern between mod and digit. I doubt it
#is necessary to test ALL digits, there must be a way
#to rule some out 

#This program spends most of its time just iterating
#through the while loop, and decrementing digit by 1
#there has to be another way to decrement quickly, and rule out
#digits

#Notice that the code only prints the digit being tested
#and its mod with n every 10-million loops. It is still slow....


#Perhaps there is a way to predict whether digit will divide n,
#ahead of time. Perhaps consider some proabability model
#to immediately rule out those which have 0 percent
#probability of dividing evenly. 

def find_LPF(n):
    if isprime1(n):
        print(n,'IS PRIME')
        return -1
    digit = n//2 #integer division to find floor of half
    loops = 0
    mod = None
    while digit > 1:
        if loops%10000000 == 0: print(digit,':',mod)
        mod = n%digit
        if mod == 0:
            print('-----',digit,'divides',n,'evenly ----')
            print('testing_primality of',digit)
            tic = T.time()
            is_prime = isprime1(digit)
            toc = T.time()
            time = toc-tic
            if time > 1: print('took',time,'seconds')
            if is_prime: return digit
            input('enter to continue')
            print('resuming')
        digit -= 1
        loops += 1
        
def test_behavior():
    n = 463664
    dig = n//2
    while dig > 1:
        print(dig,':',n%dig)
        dig -= 1
    
    
    
        

    
    
    
    
    

    
        