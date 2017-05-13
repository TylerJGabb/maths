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
 

def UPF(n):
    factors = []
    digit = n//2
    loops = -1
    while True:
        
        loops += 1
        if loops %1000000 == 0:
            print(n,':',digit)
        
        last = int(str(digit)[-1])
        if digit > 10:
            if last not in (1,3,7,9):
                digit -= 1 #if the digit is not odd
                continue   #make it odd
            if last == 5:
                digit -= 2
                continue
        mod = n%digit
        if mod == 0:
            if isprime1(digit):
                n = n//digit
                factors.append(digit)
                if n in (2,3,5,7):
                    break
                digit = n//2
                continue
        digit -= 2 if digit > 10 else 1
        if digit <= 0: break
    factors.append(n)
    return factors
    
    
def LPF(n):
    digit = n//2
    loops = -1
    while True:
        loops += 1
        #if loops %100000000 == 0: print(digit)
        if digit > 10:
            last = int(str(digit)[-1])
            if last == 5: #Numbers ending in 5 are not prime
                digit -= 2 #The possible prime will be 2 less than digit
                continue
            if last not in (1,3,7,9): #Even numbers are not prime
                digit -= 1 #the next possible prime will be 1 less than digit
                continue
        mod = n%digit
        if mod == 0:
            #print('mod zero')
            if isprime1(digit):
                return digit
        digit -= 2 if digit > 10 else 1
    assert False, 'Number given is Prime'
        
            
#DEVELOPMENT TOOL       
def test_behavior():
    n = 463664
    dig = n//2
    while dig > 1:
        print(dig,':',n%dig)
        dig -= 1
        


#Generates THE NEXT PRIME after n
def GNP(n):
    assert isprime1(n)
    dig = n + 2 #f the code makes it to this point, we need not consider evenly
    #numbers. They are NOT prime
    while True:
        if isprime1(dig): return dig #This is a lie here, this is actually very
        #complex loop
        dig += 2
        
        

        
    
    
    
    
    
    
    
    
        

    
    
    
    
    

    
        