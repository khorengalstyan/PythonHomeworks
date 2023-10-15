import math
import re

class Shape:

    def calculateArea(self):
        pass

    def calculatePerimeter(self):
        pass
    
    def about(self):
        pass




class Circle(Shape):
    def __init__(self, radius = 1):
            self.__radius = radius
    def calculateArea(self):
        return math.pi * self.__radius**2

    def calculatePerimeter(self):
        return math.pi * 2 * self.__radius

    
    def setRadius(self, radius):
        if (radius > 0):
            self.__radius = radius
    
    def getRadius(self):
        return self.__radius

    def about(self):
        print( "This is a circle with ", self.__radius, "radius")



class Rectangle(Shape):


    def __init__(self, width = 1, height = 1):
            self.width = width
            self.height = height
    def calculateArea(self):
        return self.width * self.height

    def calculatePerimeter(self):
        return 2 * self.width + 2 * self.height

    
    def setWidth(self, width):
        if (width > 0):
            self.width = width

    def setHeight(self, height):
        if (height > 0):
            self.height = height
    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

    def about(self):
        print("This is a rectangle with ", self.height, " height and ", self.width, " width.")



class Triangle(Shape):

    def __init__(self, firstSide = 3, secondSide = 4, thirdSide = 5):
            self.firstSide = firstSide
            self.secondSide = secondSide
            self.thirdSide = thirdSide
    def calculateArea(self):
        perimeter = (self.firstSide + self.secondSide + self.thirdSide) / 2
        return math.sqrt(perimeter * (perimeter - self.firstSide) * (perimeter - self.secondSide) * (perimeter - self.thirdSide))

    def calculatePerimeter(self):
        return self.firstSide + self.secondSide + self.thirdSide

    
    def setFirstSide(self, firstSide):
        if (firstSide > 0):
            self.firstSide = firstSide

    def setSecondSide(self, secondSide):
        if (secondSide > 0):
            self.secondSide = secondSide

    def setThirdSide(self, thirdSide):
        if (thirdSide > 0):
            self.thirdSide = thirdSide

    
    
    def getFirstSide(self):
            return self.firstSide
    
    def getSecondSide(self):
            return self.secondSide
    
    def getThirdSide(self):
            return self.thirdSide 

    def about(self):
        print("This is a triangle with ", self.firstSide, self.secondSide, self.thirdSide, " sides")
    

#print("Usage: This is a simple shape creator script. Please input desired shape and it's parameters")







def printUsage(shape):
    if (shape == "circle"):
        print("Usage:Circle gets radius. Circle's radius must be greater than 0.")
    elif (shape == "rectangle"):
        print("Usage:Rectangle gets width and height. Rectangle's width and height must be greator than 0.")
    elif (shape == "triangle"):
        print("Usage: Triangle gets 3 sides. Triangle's sides must be greator than 0 and summary of 2 sides must be greator than the third side.")


def shapeCreator(*args):
    validShape = 0
    if (args[0][0] == "circle"):
        if (float(args[0][1]) > 0 and len(args[0]) == 2):
            createdShape = Circle(float(args[0][1]))
            validShape = 1
     
    elif (args[0][0] == "rectangle"):
        if (float(args[0][1]) > 0 and float(args[0][2]) > 0 and len(args[0]) == 3):
            createdShape = Rectangle(float(args[0][1]), float(args[0][2]))
            validShape = 1
    elif (args[0][0] == "triangle"):
        if (float(args[0][1]) > 0 and float(args[0][2]) > 0 and float(args[0][3]) and len(args[0]) == 4):
            if (float(args[0][1]) + float(args[0][2]) > float(args[0][3]) and float(args[0][2]) + float(args[0][3]) > float(args[0][1]) and float(args[0][3]) + float(args[0][1]) > float(args[0][2])):
                createdShape = Triangle(float(args[0][1]), float(args[0][2]), float(args[0][3]))
                validShape = 1
            else:
                print("\033[33mWarning : Triangle is not valid\033[32m")
                validShape = 2
    
    

    if (validShape == 1):
        createdShape.about()
        print("Area : ", createdShape.calculateArea())
        print("Perimeter : ", createdShape.calculatePerimeter())
    elif (validShape == 0): 
        print("\033[33mWarning : Shape is not valid\033[32m")
        printUsage(args[0][0])
        




def commandLineInterface():

    while True:
        print("\033[32m")
        inputtedCommand = input("Enter your shape. You will get it's area and perimeter. Example create <Shape> [Parameters]. To finish execution please input quit\n")
        if inputtedCommand.lower() == "quit":
            exit()
        arguments = inputtedCommand.split()
        shapeCommands = arguments[1:len(arguments)]
        if (len(arguments) < 1):
            print ("\033[33mWarning: Please provide valid options.\033[32m")
        else:
            action = arguments[0].lower()
            if (action == "create"):
                shapeCreator(shapeCommands)
            print ("\033[33mWarning: Please provide valid action. Now only \"create\" action is available\033[32m")




commandLineInterface()




