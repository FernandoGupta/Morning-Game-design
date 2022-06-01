#Fernando Gupta 
#Calculate BMI
#Get user Hight in M and Weight in KG
import os
os.system ('cls')
Weight=63 #this is the weight value as a number 
Weight=float (input('ur weight')) #question for program, float is used so a decimal can be imputed
Height=('1.8') #this is the height of person without squareing as a number 
Height=float (input('ur height'))#question for program, float is used so a decimal can be imputed 
Heightsq= Height*Height #this finds height squared so the BMI formula can be used
BMI=Weight/Heightsq #This is formula for BMI
print('ur BMI is', BMI)  #this is to display your BMI