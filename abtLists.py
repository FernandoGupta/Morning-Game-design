# Fernando Gupta
# going to learn about lists,  functions related to lists 
# going to learn about for loop 
import random
import os
os.system('cls')

thislist = ["apple","bannana","cherry","orange","kiwi","melon","mango"] 
print(thislist[1]) #print from a specific index
print(thislist[-1]) #print from the end
print(thislist[2:5]) #print from two value the first one is included in the set the second is excluded
print(thislist[:3]) #print up to a value but not including a value
print(thislist[2:]) #prints everything after a value not including the origional element 
print(thislist[-4:-1])

if "apple" in thislist:
    print("yes, apple is in this list")

for num in range(10): # loops a specific number of times 
    print(num, end = " ")

print()

for element in thislist:
    print(element, end = " ") #element = thislist [times run through the loop]
print()

thislist.append("pineaple")
print(thislist[0:])

# for num in this range (2)
#       thislist.append(input("input a food"))
#print (thislist[0:])


thislist.insert(0, "pineaple") #adding an element to a specific index insert (index, element you want to add)
print(thislist[0:])

for i in range(len(thislist)): 
    print(thislist[i], end = " / ") 
print()

list_num = [1, 2, 3, 4]
list_num.extend(thislist)
print(list_num)

list_num = [1, 2, 3, 4]
list_num.append (thislist)
print(list_num)
print(list_num[-1]) #print the last element 
print(list_num[-1][-0]) # print a element in in an element if tha 

# for i in range(5):  this allows u to make it pic more dan once 
word = random.choice(thislist) #selects random elements from list 
print(word)

guess = input('input a food')
if guess in word:
    print("nice you got the word")

