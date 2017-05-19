'''
Contains several modules for encrypting and decrypting messages and sequences

Utilizes functions from primes_module

PROBLEMS: extended euclidian algorithm is correct, however, trying
to decrypt after having used a 40 bit key means taking powers on orders of
10^100 or 10^1000...0
'''

import primes_module as Primes 
import math
import random
import string
##HURDLES TO GET OVER:
## (1) generating large primess
## (2) taking large powers, or getting a reasonable 
##     back_power while preserving encryption strength
##      

PRINTABLE = string.printable
LITTLE = string.ascii_lowercase
BIG    = string.ascii_uppercase
WHITE  = string.whitespace
PUNCT  = string.punctuation
CHARS = LITTLE + BIG + WHITE + PUNCT
ENCODE = {PRINTABLE[i]:i+1 for i in range(len(PRINTABLE))}
NUMBERS = [1,2,3,4,5,6,7,8,9,0]
ENCODE_REV = {ENCODE[key]:key for key in ENCODE}  


     
#Encrypts a string s with exponent e and mod key
def encrypt(s,e,key):
    ##KEY IS PRODUCT OF TWO PRIMES
    encrypted = [ENCODE[m]**e%key for m in s]
    jarb_list = [c%len(ENCODE) + 1 for c in encrypted]
    jarbled = ''.join([ENCODE_REV[c] for c in jarb_list])
    print('Jarbled message:',repr(jarbled)) #Just for fun
    return (encrypted)
    
def decrypt(L,d,key):
    print('DECRYPTING...MAY TAKE HECKIN LONG TIME')
    unlocked = [ENCODE_REV[c**d%key] for c in L]
    return ''.join(unlocked)
    
 
#This takes a long time if bits greater than 20
#Perhaps consider havbing a databse of prime numbers 
def generate_key(bits):
    #print('Generating key, this may take a while, please be patient')
    prime_length = bits//2
    p1 = generate_prime(prime_length)
    p2 = generate_prime(prime_length)
    n = p1*p2
    phi = (p1-1)*(p2-1)
    e = generate_exp(phi)
    d = extended_euclidian_algorithm(phi,e) ##CAUSING PROBLEMS
    key = (n,e,d)
    fwd_pow = e
    bck_pow = d
    mod_key = n
    '''
    print("Forward Power: ",fwd_pow)
    print("Backward Power:",bck_pow)
    print("Modulo Key:    ",mod_key)
    '''
    return (mod_key,fwd_pow,bck_pow)
    
#generates a random prime number, of length half_bits   
def generate_prime(half_bits):
    assert type(half_bits) == int
    num = ''
    for i in range(half_bits):
        num += str(random.choice(NUMBERS))
    num = int(num)
    return Primes.GNP(num)

def generate_exp(phi):
    #returns a number which is not a factor of phi
    #starts at 1 and counts up
    mod = 0
    e = 2
    while mod == 0:
        e += 1
        mod = phi%e #if mod != 0, then e is not a factor
                    #loop will break if mod != 0, and e will be returned
    return e
        
#algorithm developed by euclid before computers even existed
#in order to find the decryption power        
def extended_euclidian_algorithm(phi,e):
    assert phi%e != 0
    left_col  = [phi,e]
    right_col = [phi,1]
    while left_col[-1] != 1:

        L_top = left_col[-2]
        L_bottom = left_col[-1]
        R_top = right_col[-2]
        R_bottom = right_col[-1]        
        
        c = L_top//L_bottom
        
        L_new = L_top - L_bottom*c
        R_new = R_top - R_bottom*c
        
        if L_new < 0: L_new = L_new%phi
        if R_new < 0: R_new = R_new%phi
        
        left_col.append(L_new)
        right_col.append(R_new)
        '''
        print(left_col)
        print(right_col)
        print('----------')
        '''
    d = right_col[-1]
    return d

#obtains a key with a resonable inverse    
def get_reasonable_key(N):
    ##Seemingly never ends
    bck_pow = 100000
    key_len = N//2
    while True:
        try:
            (key,fwd_pow,bck_pow) = generate_key(N)
        except ZeroDivisionError: #Still don't know what causes this error btw
            continue
        key_len = len(str(key))
        if bck_pow <= 99999:# and key_len in range(N-2,N+3):
            print('-'*10)
            print('Key Generated:')
            print('modulo key =   ',key)
            print('locking key =  ',fwd_pow)
            print('unlocking key =',bck_pow)
            print('-'*10)
            return (key,fwd_pow,bck_pow)
            
#turns a list into a string
def list2str(L): return "" if not L else str(L[0]) + list2str(L[1:])
            
############################################################################
##                DEMOS        DEMOS          DEMOS                      ###
############################################################################
def DEMO():
    file = open('DemoText.txt','r')
    for line in file: print(line.strip())
    msg = input('Input msg: ')
    (key,e,d) = get_reasonable_key(6)
    locked = encrypt(msg,e,key)
    print('What your msg was turned into:')
    print(locked)
    input('Enter to decrypt...')
    unlocked = decrypt(locked,d,key)
    print('Decrypted msg:',unlocked)
    


    
    
    
    
    
        
    
    
    
    
'''
KEY = p1 * p2
PHI = (p1-1)*(p2-1)
pick an expbonent e (your key)
PHI MUST NOT SHARE A FACTOR WITH e
find inverse of e, which is d
(e*d) mod PHI = 1 SOLVE THIS EQUATION FOR d

then can use d to decrypt:

m**e%n = c
c**d%n = m
done...
'''



    
    
    
