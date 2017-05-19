##8 BIT ENCRYPTION DEMO FILE##

import sys

try:
    from encryption import *
except (ImportError):
    print("MISSING FILES ERROR:")
    print("make sure you have the following files in the same directory:")
    print("encryption.py")
    print("primes_module.py")
    print("DemoText.txt")
    input('Enter to exit...')
    sys.exit(1)
        
try:       
    DEMO()
except (FileNotFoundError):
    print("Need DemoText.txt in the same directory. Exiting")
    input('Enter to exit...')
    sys.exit(1)
input('Enter to exit')
