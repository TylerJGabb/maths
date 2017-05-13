This project is mainly concerned with prime numbers and developing
fast algorithms for factoring them. 

As of right now 8:22 pm, may,12,2017, the find_LPF function is wrong
the function is finding the wrong thing, it is finding the largest
prime which divides n ahd has a remainder of 0, not the largest prime factor.

a number n divides m evenly iff m/n in {integers}

even division is not defined by mod(m,n) = 0
