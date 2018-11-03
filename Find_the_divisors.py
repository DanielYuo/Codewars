#Find the divisors! 
#Level: 7kyu

'''
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. 
If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
'''

def divisors(integer):
    num = []
    for i in range(2, integer-1):
        if integer % i == 0:
            num.append(i)
            
    if len(num) == 0:
            return (str(integer) + ' is prime')
    else:
         return num 
