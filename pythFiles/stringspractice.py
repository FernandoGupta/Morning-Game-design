#Fernando Gupta
#we are going to learn about strings    "or"
import os
os.system ('cls')
print('hi')
print("Hi")
print("hi, lets go to the park")
message="you are awesome"
#      0 1 2 3 4 5     all arrays begin in zero
#       H e l l o 
print(message)
print(message[5])   # print teh letter in position 5
print(message[0:5]) # print all letter from position 0 to 4 5 characters
if message.isdigit (): #isdigit  is a method you must use it with a dot 
    sum=message +3 #if teh statement is tru 
else:
    print (message+ " i say so")
print (message.upper())
print(message)
if message.isupper():
    print(message)
else:
    # print("i am false") #use only for debugging i will delete or com when finished 
    message=message.upper()
    print(message)
print(type(message))
print(dir(message))
