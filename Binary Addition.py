#Binary Addition
#Level: 7kyu

'''
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.
'''

def add_binary(a,b):
    x = a + b 
    binax = bin(x)
    return binax[2:]
