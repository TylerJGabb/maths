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
import largest_prime_factor as Primes
import matplotlib.pyplot as pyp


class Input:
    num_to_gen = None #Number of primes to generate after start number
    start = None #Number to begin generatuing primes after
    output_format = None #this option specifies what format the data should be
                         #output as. EX: csv, txt, png-plot. 
    options = []
    #The Input class. Purpose is to facilitate input from the user to 
    #set up experiment.
    @classmethod
    def get_bounds(cls):
        varlist = [cls.start,cls.num_to_gen]
        msg_list = ['Start number: ','Primes to generate: ']
        for i in (0,1):
            correct_input = False
            while not correct_input:
                varlist[i] = input(msg_list[i])
                try:
                    varlist[i] = int(varlist[i])
                    assert varlist[i] >= 1
                except (ValueError,AssertionError):
                    print('INVALID ENTRY: Enter integer greater than 0')
                    continue
                correct_input = True
        
   
    #I don't think the block of code below is necessary
    '''
   @classmethod
    def get_output_format(cls):
        print('How would you like to output your data?')
        print('Options:')
        options = ['csvfile','plot png (time vs size of number)',
                   'plain .txt','...more to come...','something else']
        i = 0           
        for option in options:
            i += 1
            print(i,option)
        
        correct_input = False
        while not correct_input:
            choice = input('Enter option (1 thru ' + str(i) + '): ')
            try:
                choice = int(choice)
                assert choice in range(1,i+1)
            except (AssertionError,ValueError):
                print('INVALID ENTRY: Enter integer between 1 and '+str(i))
                continue
            correct_input = True
            
        cls.options = options
        cls.output_format = options[choice-1]
        '''
    
class Experiment:
    @classmethod
    def generate_data(cls,start,num_to_gen,filename = None):
        #consider keeping track of gaps between primes
        #time how long it takes to generate, then subsequently factor
        for i in range(num_to_gen):
            #Each round of repetition will
            #1) Generate the next prime
            #2) Factor the prime
            #During steps 1 and 2, each operation is timed
            #File output lines will appear as : Number, Generation, Factorization
            gen_tic = time.time()
            next_prime = Primes.GNP(start)
            gen_toc = time.time()
            
            gen_time = gen_toc-gen_tic)
            if gen_time < 10**(-3):
                #do some stuff to make the data collected more reliable.
                #maybe new standalone function...
                pass
            factor_tic = time.time()
            factors = Primes.UPF(next_prime)
            factor_toc = time.time()
            start = next_prime
            
            
        
    
    
    
    
    
def main():
    Input.get_bounds()
    Input.get_output_format()

    
    
    
    
    
    
    
    
    
    
    
    
    