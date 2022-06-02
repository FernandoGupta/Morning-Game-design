# Fernando Gupta
#strings hw
# write question 
# write method used
# strings,arrays, length, methods and imput

import os
os.system('cls')

# Problem 1 A Write a program to create a new string made of an input string’s first, middle, and last character. 
#given string is james, extected output is Jms
word=input('ur word is ') #get word
number=(len(word)) #get numbers of letters in word
first = word[0] #first letter of word
middlenumber = int(number/2) #number of middle digit of workd
middle = word[middlenumber] #middle letter of word
last = word[number-1] #get last letter of word
print(first+middle+last) #print letters together 

# problem 1 B Write a program to create a new string made of the middle three characters of an input string. 
# Case 1 given is JohnDipPeta, expected output is Dip
word=input('ur word is ') #get word
number= len(word) #number of letters 
middle2= number//2
print('the middle 3 characters are:', word[middle2-1]+word[middle2]+word[middle2+1])

# Case 2 given is JaSonAy, expected output is Son
word=input('ur word is ') #get word
number= len(word) #number of letters 
middle2= number//2
print('the middle 3 characters are:', word[middle2-1]+word[middle2]+word[middle2+1])
 
# Problem 2 Given two strings,s1ands2. Write a program to create a new string s3 by appending s2 in the middle of s1.
# Case 1 Given S1="Ault" S2="Kelly" expected output AuKellylt 
word1=input('ur first word is ') #get word 
word2=input('ur second word is ') # get second word
number=len(word1) # number of letters in first word
firstpart= word1[:number//2] #to find first half of word
secondpart= word1[number//2:] #to find second half of word 
print('the new string is:', firstpart+word2+secondpart) #desplay new string with the 
# Problem 3 Given two strings,s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.
# Given S1=America S2=Japan Expected output AJrpan
wordA= input('ur first word is ') #get word 
wordB=input('ur second word is ') # get second word
numberA=(len(wordA)) #get numbers of letters in word
numberB=(len(wordB))
firstA = wordA[0] #first letter of word
middlenumberA = int(numberA/2) #number of middle digit of workd
middleA = wordA[middlenumberA] #middle letter of word
lastA = wordA[numberA-1] #get last letter of word
firstB = wordB[0] #first letter of word
middlenumberB = int(numberB/2) #number of middle digit of workd
middleB = wordB[middlenumberB] #middle letter of word
lastB = wordB[numberB-1] #get last letter of word
print('the new string is:', firstA+firstB+middleA+middleB+lastA+lastB)
# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
# Given PyNaTive Expected output is yaivePNT
word=input('ur word is') #get word 
uppercase=''.join([c for c in word if c.isupper()])
lowercase=''.join([c for c in word if c.islower()])
print ('this is the new string:', lowercase+uppercase)