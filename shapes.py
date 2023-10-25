import math


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
            self.__width = width
            self.__height = height
    def calculateArea(self):
        return self.__width * self.__height

    def calculatePerimeter(self):
        return 2 * self.__width + 2 * self.__height

    
    def setWidth(self, width):
        if (width > 0):
            self.__width = width

    def setHeight(self, height):
        if (height > 0):
            self.__height = height

    def getHeight(self):
        return self.__height

    def getWidth(self):
        return self.__width

    def about(self):
        print("This is a rectangle with ", self.__height, " height and ", self.__width, " width.")


class Triangle(Shape):

    def __init__(self, firstSide = 3, secondSide = 4, thirdSide = 5):
            self.__firstSide = firstSide
            self.__secondSide = secondSide
            self.__thirdSide = thirdSide
    def calculateArea(self):
        perimeter = (self.__firstSide + self.__secondSide + self.__thirdSide) / 2
        return math.sqrt(perimeter * (perimeter - self.__firstSide) * (perimeter - self.__secondSide) * (perimeter - self.__thirdSide))

    def calculatePerimeter(self):
        return self.__firstSide + self.__secondSide + self.__thirdSide

    
    def setFirstSide(self, firstSide):
        if (firstSide > 0):
            self.__firstSide = firstSide

    def setSecondSide(self, secondSide):
        if (secondSide > 0):
            self.__secondSide = secondSide

    def setThirdSide(self, thirdSide):
        if (thirdSide > 0):
            self.__thirdSide = thirdSide

    
    def getFirstSide(self):
            return self.__firstSide

    def getSecondSide(self):
            return self.__secondSide

    def getThirdSide(self):
            return self.__thirdSide 

    def about(self):
        print("This is a triangle with ", self.__firstSide, self.__secondSide, self.__thirdSide, " sides")




        
        

class ShapeManager:
    def __init__(self):
        self.createdShapes = []
        self.shapes = {
            'circle' : self.circleCreator,
            'triangle' : self.triangleCreator,
            'rectangle' : self.rectangleCreator
        }

    
    def validShape(self, *shape):
        shapeName = shape[0][0]
        isValid = True
        if (shapeName == "circle"):
            if (float(shape[0][1]) <= 0 or len(shape[0]) != 2):
                isValid = False
        elif (shapeName == "rectangle"):
            if ((float(shape[0][1]) <= 0 or float(shape[0][2]) <= 0) or len(shape[0]) != 3):
                isValid = False
        elif (shapeName == "triangle"):
            if (float(shape[0][1]) <= 0  or float(shape[0][2]) <= 0 or float(shape[0][3]) <= 0 or len(shape[0]) != 4):
                isValid = False
        
        return isValid
    
    def circleCreator(self, *shape):
        shape = Circle(float(shape[0][1]))
        return shape


    def triangleCreator(self, *shape):
        shape = Triangle(float(shape[0][1]), float(shape[0][2]), float(shape[0][3]))
        return shape
    
    def rectangleCreator(self, *shape):
        shape = Rectangle(float(shape[0][1]), float(shape[0][2]))
        return shape

    
    def shapeCreator(self, *shape):
        shapeName = shape[0][0]
        if (self.validShape(shape[0]) == True):
            createdShape = self.shapes[shapeName](shape[0])
            self.createdShapes.append(createdShape)
        else:
            self.printUsage(shapeName)
    

    def printUsage(self, shape):
        if (shape == "circle"):
            print("Usage:Circle gets radius. Circle's radius must be greater than 0.")
        elif (shape == "rectangle"):
            print("Usage:Rectangle gets width and height. Rectangle's width and height must be greator than 0.")
        elif (shape == "triangle"):
            print("Usage: Triangle gets 3 sides. Triangle's sides must be greator than 0 and summary of 2 sides must be greator than the third side.")
    

    
    def printShapes(self):
        for shape in self.createdShapes:
            
                shape.about()
                print("Area : ", shape.calculateArea())
                print("Perimeter : ", shape.calculatePerimeter())
                print("\n")


      
shapeManager = ShapeManager()


def commandLineInterface():

    while True:
        print("\033[32m")
        inputtedCommand = input("Enter your action. You can create shape with \"create <Shape> [parameters]\" or get info about shapes with \"shapes\" command.Please input \"quit\" to finish execution.\n")
        if inputtedCommand.lower() == "quit":
            exit()
        arguments = inputtedCommand.split()
        shapeCommands = arguments[1:len(arguments)]
        if (len(arguments) < 1):
            print ("\033[33mWarning: Please provide valid options.\033[32m")
        else:
            action = arguments[0].lower()
            if (action == "create"):
                shapeManager.shapeCreator(shapeCommands)
            elif (action == "shapes"):
                shapeManager.printShapes()
                
            else:
                print ("\033[33mWarning: Please provide valid action. Now only \"create\" and \"shapes\" actions are available\033[32m")

commandLineInterface()
