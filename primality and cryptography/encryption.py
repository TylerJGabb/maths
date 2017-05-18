'''
Contains several modules for encrypting and decrypting messages and sequences

Utilizes functions from primes_module
'''
import primes_module as Primes #BELOW WAS MADE IN HASKELL
import math
import random
'''

'''
NUMBERS = [1,2,3,4,5,6,7,8,9,0]
upper_tupe_encode = [('A',1),('B',2),('C',3),('D',4),('E',5),('F',6),('G',7),('H',8),('I',9),('J',10),('K',11),('L',12),('M',13),('N',14),('O',15),('P',16),('Q',17),('R',18),('S',19),('T',20),('U',21),('V',22),('W',23),('X',24),('Y',25),('Z',26)]
lower_tupe_encode = [(a[0].lower(),26+a[1]) for a in upper_tupe_encode]
encode_raw = upper_tupe_encode + lower_tupe_encode   
ENCODE = {a[0]:a[1] for a in encode_raw}
ENCODE[' '] = 26*2 + 1  
ENCODE_REV = {ENCODE[key]:key for key in ENCODE}  
def list2str(L):
    s = ""
    for x in L:
        s += str(x)
    return s
    
def main():
    msg = input('Input msg to encrypt: ')
    msg_list = list(msg)
    numbers = [ENCODE[x] for x in msg_list]
    numbers = [num**3 for num in numbers]
    numbers = [num%10 for num in numbers]
    encryption = list2str(numbers)
    print('ENCRYPTED:',encryption)
    
    new_numbers = [(num**3)%10 for num in numbers]
    print('DECRYPTED:',new_numbers)
 
#Encrypts a string s with exponent e and mod n
def encrypt(s,e,key):
    ##KEY IS PRODUCT OF TWO PRIMES
    encrypted = [ENCODE[m]**e%key for m in s]
    #encrypted_letters = [ENCODE_REV[x] for x in encrypted]
    #return ''.join(encrypted_letters)
    return encrypted
 
#This takes a long time if bits greater than 20
#Perhaps consider havbing a databse of prime numbers 
def generate_key(bits):
    print('Generating key, this may take a while, please be patient')
    prime_length = bits//2
    p1 = generate_prime(prime_length)
    p2 = generate_prime(prime_length)
    n = p1*p2
    phi = (p1-1)*(p2-1)
    e = generate_exp(phi)
    d = extended_euclidian_algorithm(phi)
    return (p1,p2,n,phi,e,d)
    
#generates a random prime number, of length half_bits   
def generate_prime(half_bits):
    assert  type(half_bits) == int
    num = ''
    for i in range(half_bits):
        num += str(random.choice(NUMBERS))
    num = int(num)
    return Primes.GNP(num)

def generate_exp(phi):
    #returns a number which is not a factor of phi
    #starts at 1 and counts up
    mod = 0
    e = 1
    while mod == 0:
        e += 1
        mod = phi%e #if mod != 0, then e is not a factor
                    #loop will break if mod != 0, and e will be returned
    return e
        
        
def extended_euclidian_algorithm(phi):
    d = None
    return d
    
    
        
    
    
    
    
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



    
    
    
