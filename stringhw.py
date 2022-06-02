# Fernando Gupta
#strings hw
# write method used
# write question 


import os
os.system('cls')

# Problem 1 A Write a program to create a new string made of an input string’s first, middle, and last character. 
#given string is james, extected output is Jms
message=("James")
print(message[0], end="")
print(message[2], end="")
print(message[4])

# problem 1 B Write a program to create a new string made of the middle three characters of an input string. 
# Case 1 given is JohnDipPeta, expected output is Dip
message2=("JohnDipPeta")
print(message2[4:7])
# Case 2 given is JaSonAy, expected output is Son
message3=("JaSonAy")
print(message3[2:5])
# Problem 2 Given two strings,s1ands2. Write a program to create a new string s3 by appending s2 in the middle of s1.
# Case 1 Given S1="Ault" S2="Kelly" expected output AuKellylt
message4=('Ault')
message5=('Kelly')
print(message4[0:2]+message5+message4[2:4])
# Problem 3 Given two strings,s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.
# Given S1=America S2=Japan Expected output AJrpan
message6=("America")
message7=("Japan")
print(message6[0]+message7[0]+message6[3]+message7[2]+message6[6]+message7[4])
# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
# Given PyNaTive Expected output is yaivePNT
message8=("PyNaTive")
print(message8[1]+message8[3]+message8[5:8]+message8[0]+message8[2]+message8[4])