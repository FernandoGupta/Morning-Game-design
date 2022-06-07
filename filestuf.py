# Fernando Gupta
# Learning abt files
# r, read 
# A, append
# W, write 
# 
# open files, make sure to close a file 

import os, datetime
os.system("cls")
name="fernando"
score= 120
date=datetime.datetime.now() #todays date and time
print(date.strftime("%m/%d/%Y"))
print(date.strftime("%Y/%m/%d"))
screline=str(score) + "\t"+name+"\t"+ date.strftime("%m/%d/%Y")
screeline2 = str(score) + "\t"+"monke"+"\t"+date.strftime("%m/%d/%Y")
print(screline)
myFile=open("scre.txt",'w') #this opens the file to write 
myFile.write(screline)
myFile.close()
myFile=open("scre.txt",'a') #this opens the file to edit but not rewrite 
myFile.write(screline)
myFile.close()
myFile=open("scre.txt",'w')
myFile.write(screeline2)
myFile.close()
myFile=open("scre.txt",'r') #this opens a file to read
# lines=myFile.readlines()
print()
for line in myFile.readlines():
    print(line)
myFile.close()
