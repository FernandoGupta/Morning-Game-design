# Fernando Gupta
# write a code to find if the number is even or odd, and if it a multiple of 3

import os
os.system('cls')

number=int(input("ur number is "))

if(number%2==0):
    print(number,'is an even number')
else:
    print(number,'is an odd number')

# multiple of number section
if(number%3==0):
    print(number,'is a multiple of 3')
else:
    print(number,'is not a multiple of 3')

if(number%5==0):
    print(number,'is a multiple of 5')
else: 
    print(number,'is not a multiple of 5')
