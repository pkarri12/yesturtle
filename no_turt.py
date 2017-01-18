#import the turtle library
import turtle

#Declare your varibles
nbrSides = 0
lengthOfLines = 50

#Ask for input from the user
#Need to make sure we want to convert that to an integer value as input gives us a string
nbrSides =int(input("Please specify how many sided-object you want? "))

#Make a for loop to create an object
for steps in range(nbrSides):
	turtle.forward(lengthOfLines)
	turtle.right(360/nbrSides)
	turtle.color("green")
#Make another inside loop so it creates objects in object
	for moreSteps in range(nbrSides):
		turtle.forward(lengthOfLines/2)
		turtle.right(360/nbrSides)
		
	


