'''
Purpose of this code is to accurately measure the time it takes
to generate new primes, compared to factoring said primes. 

Primes will be generated, from some number n, to some number k,
and each prime that is generated will then be factored.

All of these measured attributes will be output to a file, to be
able to plot and view. Of course, it is obvious that as the numbers
get larger, the time taken to either generate or factor will be
compounded, the question is how much, and how fast.

If I can find access to some remote super-computer, I will do this for larger
numbers. 

I feel I should mention that I know python is not the right language for this
it would be more appropriate to do this in C, or another language which
is closer to the machine. I'm sure python does many things in the backround
even though It may or may not be neeeded. 
'''
import time
import math
import largest_prime_factor as LPF

class Input:
    #The Input class. Purpose is to facilitate input from the user to 
    #set up experiment.
    pass
    
class Experiment:
    #The Experiment class. Methods here will be used to actually run code
    #conduct experiments.
    pass
    