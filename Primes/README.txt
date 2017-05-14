This project is mainly concerned with prime numbers and developing
fast algorithms for factoring them. 

*MET GOAL: adding Unique prime facoritazion function
*MET GOAL: find largest prime factor the fastest way in python
*NEW GOAL: Streamline decrement in UPF, to skip nonprime numbers

5/13/2017--------------------------------------------

*Fixed UPF (unique prime factorization function)
*Fixed LPF (largest prime factor function)
*Fixed GNP (generate next prime function) to work for any positive integer
*Added profiler.py file, containing methods to be used for running experiments
    to generate plots and timing profiles for the functions
    
TO ACCESS THBE FUNCTIONS, IN CONSOLE TYPE:
from profiler import *

after you have done this, you will have access to the functions
via the following

Primes.LPF(n), gives the largest prime factor of n
Primes.GNP(n), gives THE NEXT PRIME after the integer n
Primes.UPF(n), returns a list, containing the unique prime factors of n

---END OF 5/15/2017 UPDATE------------------------------------

Although Python is not the right language for trying to write FAST algorithms to do this,
if I can find a way to impliment it in python, moving to a faster language will be easier.
