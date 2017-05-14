import sys
import math as M
import time as T
##What is the largest prime factor of a number n
##Prime numbers, if they are more than 1 digit, end in 
## 1,3,7,9

def isprime1(n):
    #print('testing primality')
    if n < 10: 
        #print('stage1')
        return n in (2,3,5,7)
    if int(str(n)[-1]) not in (1,3,7,9):
        #print('stage2')
        return False 
    top = M.floor(M.sqrt(n))
    #print('stage3')
    #print(top)
    i = 0
    for digit in range(2,top+1):
        #if i%10000 == 0: print('loop',i,digit)
        if n%digit == 0: return False
        i += 1
    return True
 
#returns the unique prime factorization of a given number
def UPF(n):
    factors = []
    digit = n//2
    loops = -1
    while True:
        loops += 1
        if loops%1000000 == 0:
            print(n,':',digit)
        
        last = int(str(digit)[-1])
        if digit > 10:
            if last not in (1,3,7,9) and last != 5: ##FIX THIS
                digit -= 1 #if the digit is not odd
                continue   #make it odd
            elif last == 5:
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
    mod = '?'
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
        assert digit > 0,str(n)+' is prime'
        mod = n%digit
        if mod == 0:
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
    if n == 2: return 3
    if n == 3: return 5
    if n == 5: return 7
    if n == 7: return 11
    last = int(str(n)[-1])
    n += 1 if last%2 == 0 else 2
    assert int(str(n)[-1]) % 2 != 0
    while True:
        #print(n)
        if isprime1(n): return n
        n += 2 if str(n)[-1] != '3' else 4
        

        
    
    
    
    
    
    
    
    
        

    
    
    
    
    

    
        