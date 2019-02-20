"""
This project is a calculator that can compute the area of a given shape, as selected by the user. The calculator is able to determine the area of the following shapes:
- Circle
- Triangle
The program does the following:
1. Prompt the user to select a shape
2. Depending on the shape the user selects, calculates the area of that shape
3. Print the area of that shape to the user
"""
#Importing necessary Python libraries
from math import pi
from time import sleep
from datetime import datetime

#User feedback that session is starting
now = datetime.now()
print "Calculator is starting up..."
print "Current time is: %s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute)

sleep(1)
hint = "Don't forget to include the correct units! \nExiting..."

option = raw_input("Enter C for Circle or T for Triangle: ")
option = option.upper()

if option == 'C':
  radius = float(raw_input("What is the radius of the circle? "))
  area = pi * radius ** 2
  print "The pie is baking..."
  sleep(1)
  print ("Area: %.2f \n%s" % (area, hint))
elif option == 'T':
  base = float(raw_input("What is the base of the triangle?"))
  height = float(raw_input("What is the height of the triangle?"))
  area = 0.5 * base * height
  print "Uni Bbi Tri..."
  sleep(1)
  print ("Area: %.2f \n%s" % (area, hint))
else:
  print "Error! Invalid shape selector specified. Exiting..."