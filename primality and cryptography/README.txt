This project is mainly concerned with prime numbers and developing
fast algorithms for factoring them. 

*MET GOAL: adding Unique prime facoritazion function
*MET GOAL: find largest prime factor the fastest way in python
*MET GOAL: Streamline decrement in UPF, to skip nonprime numbers
*NEW GOAL(5/16): Research algorithms for prime factorization and prime seive, devlop several
	functions which impliment different algorithms, and compare their results for numbers
	whose digit counts are between 1 and 20
*NEW GOAL: begin developing keys for encrypting messages. 

5/18/2017
Began working with haskell. It is a work in progress. 

5/16/2017-----------------------------------------
SEE NEW GOAL(5/16)
Added some classes and methods in the profiler module. Analysis class takes care of
Analyzing generated data. Planning on making it universal, checking the file for 
any erroneous data, and getting input from the user, recursively, until every
attribute of the data given can be assigned accordingly


5/15/2017-------------------------------------------
I've managed to perform the first few experiments. As far as I can tell, There was some flawed
thinking on my part. I was trying to generate new prime numbers and then factor them, however
primes can not be factored, so I don't trust the results aquired.

I think I need to re-think what I am trying to measure here



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

---END OF 5/13/2017 UPDATE------------------------------------

Although Python is not the right language for trying to write FAST algorithms to do this,
if I can find a way to impliment it in python, moving to a faster language will be easier.
