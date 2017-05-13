import sys
import math as M
import time as T
##What is the largest prime factor of a number n
##Prime numbers, if they are more than 1 digit, end in 
## 1,3,7,9

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
 

def LPF(n):
    #Need to start with 2, and move up to find next prime factors
    #Then when done factoring, return the largest factor....
    #That's what makes this take a while. Perhaps consider a recursive function
    
        
#DEVELOPMENT TOOL       
def test_behavior():
    n = 463664
    dig = n//2
    while dig > 1:
        print(dig,':',n%dig)
        dig -= 1
        


#Generates THE NEXT PRIME after n
def getNextPrime(n):
    assert isprime1(n)
    dig = n + 2 #f the code makes it to this point, we need not consider evenly
    #numbers. They are NOT prime
    while True:
        if isprime1(dig): return dig #This is a lie here, this is actually very
        #complex loop
        dig += 2
        
    
    
    
    
    
    
    
    
        

    
    
    
    
    

    
        