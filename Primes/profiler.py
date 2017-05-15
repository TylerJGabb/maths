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
import numpy


class Input:
    num_to_gen = None #Number of primes to generate after start number
    start = None #Number to begin generatuing primes after
    output_format = None #this option specifies what format the data should be
                         #output as. EX: csv, txt, png-plot. 
    options = []
    fname = ''
    #The Input class. Purpose is to facilitate input from the user to 
    #set up experiment.
    @classmethod
    def get_bounds(cls):


        correct_input = False
        while not correct_input:
            start = input('Enter start number: ')
            try:
                start = int(start)
                assert start >= 1
            except (ValueError,AssertionError):
                print('INVALID ENTRY: Enter integer greater than 0')
                continue
            correct_input = True
        cls.start = start
        
        correct_input = False
        while not correct_input:
            num_to_gen = input('Enter number of primes to generate: ')
            try:
                num_to_gen = int(num_to_gen)
                assert num_to_gen >= 1
            except (ValueError,AssertionError):
                print('INVALID ENTRY: Enter integer greater than 0')
                continue
            correct_input = True   
        cls.num_to_gen = num_to_gen

                
    @classmethod
    def get_fname(cls):
        cls.fname = input('Filename to write to: ')
        
        
   
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
    def experiment1(cls,start,num_to_gen,fname):
        #consider keeping track of gaps between primes
        #time how long it takes to generate, then subsequently factor
        file = open(fname,'w')
        delta = start//10
        #if not Primes.isprime1(start): ##START AT THE NEAREST
            #start = Primes.GNP(start)  ##PRIME NUMBER
           
        for i in range(num_to_gen):
            #Each round of repetition will
            #1) Generate the next prime
            #2) Factor the prime
            #During steps 1 and 2, each operation is timed
            #File output lines will appear as : Number, Generation, Factorization
            gen_tic = time.time()
            next_prime = Primes.GNP(start+delta)
            gen_toc = time.time()
            
            generation_time = gen_toc-gen_tic
            if generation_time < 5*10**-3: #less than 1ms
                #do some stuff to make the data collected more reliable.
                #maybe new standalone function which generates the number
                #over and over, need to consider overhead costs in this case
                
                #IDEAS:
                    #Keep timing generation untl epsila of mean drops below 0.002
                    ##Not sure if this idea is the best, need to pinpoint
                    ##exactly which attribute to measure error for, which will
                    ##determine the rigidity of the dataset. Of course if the
                    ##mean is not changing by more than 0.002 percent then this
                    ##would indicate that the value is settling.
                    
                    #Just time a whole bunch of times, divide the sum of time
                    #by the number of generations, taking away overhead cost   
                overhead = cls.get_overhead(100)
                toc = time.time()
                for i in range(100):
                    Primes.GNP(start)
                tic = time.time()
                generation_time = (tic-toc-overhead)/100
                    
                
            factor_tic = time.time()
            factors = Primes.UPF(next_prime)
            factor_toc = time.time()
            
            factor_time = factor_toc - factor_tic
            if factor_time <= 10**-3: #less than 1ms
                #Do some stuff to make the data more reliable
                pass
                
            line = str(next_prime) + ',' + str(generation_time) +\
                   ',' + str(factor_time) + '\n'
            file.write(line)
            start = next_prime
              
        file.close()
    @classmethod
    def get_overhead(cls,niter):
        toc = time.time()
        for i in range(niter):
            pass
        tic = time.time()
        return tic-toc
    
    
   
    
def main():
    Input.get_bounds()
    Input.get_fname()
    Experiment.experiment1(Input.start,Input.num_to_gen,Input.fname)
    

    
    
    
    
    
    
    
    
    
    
    
    
    