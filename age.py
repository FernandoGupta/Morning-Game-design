#Fernando Gupta 
#Calculate age
#get user year and current year 
import os
os.system('cls')
by=2006 #assign this value as a number 
#by=input('year y were born') give us a 
by=int (input('year y were born')) #typecast 
CurrentYear=2022
age=CurrentYear-by
print('your age is ', age)
#selection
if age >50:
    print (' U are old')    