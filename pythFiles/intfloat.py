# Fernando Gupta
# write a code to find if the number is even or odd, and if it a multiple of 3

import os
os.system('cls')

number=int(input("ur number is ")) # get number from user 

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

if(number%5==0) and (number%3==0): #if and compound question to find if it is both an multiple of 3 and 5
    print(number,'is a multiple of 5 and 3')
else: print(number,'is not a multiple of 5 and 3')
    
