import math


class Shape:

    def calculateArea(self):
        pass

    def calculatePerimeter(self):
        pass
    
    def about(self):
        pass




class Circle(Shape):
    def __init__(self, radius):
            self.__radius = radius
    def calculateArea(self):
        return math.pi * self.__radius**2

    def calculatePerimeter(self):
        return math.pi * 2 * self.__radius

    
    def setRadius(self, radius):
        if (radius > 0):
            self.__radius = radius
    
    @property
    def getRadius(self):
        return self.__radius

    def about(self):
        print( "This is a circle with ", self.__radius, "radius")



class Rectangle(Shape):


    def __init__(self, width, height):
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

    @property
    def getHeight(self):
        return self.__height

    @property
    def getWidth(self):
        return self.__width

    def about(self):
        print("This is a rectangle with ", self.__height, " height and ", self.__width, " width.")


class Triangle(Shape):

    def __init__(self, firstSide, secondSide, thirdSide):
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

    
    @property
    def getFirstSide(self):
            return self.__firstSide

    @property
    def getSecondSide(self):
            return self.__secondSide

    @property
    def getThirdSide(self):
            return self.__thirdSide 

    def about(self):
        print("This is a triangle with ", self.__firstSide, self.__secondSide, self.__thirdSide, " sides")


class ShapeManager:
    def __init__(self):
        self.shapes = []

    def printUsage(self,shape):
        if (shape == "circle"):
            print("Usage:Circle gets radius. Circle's radius must be greater than 0.")
        elif (shape == "rectangle"):
            print("Usage:Rectangle gets width and height. Rectangle's width and height must be greator than 0.")
        elif (shape == "triangle"):
            print("Usage: Triangle gets 3 sides. Triangle's sides must be greator than 0 and summary of 2 sides must be greator than the third side.")

    def shapeCreator(self, *shape):
        validShape = 0
        shapeName = shape[0][0]
        shapeSizes = shape[0][1:len(shape[0])]
        if (shapeName == "circle"):
            if (float(shapeSizes[0]) > 0 and len(shapeSizes) == 1):
                createdShape = Circle(float(shapeSizes[0]))
                validShape = 1
     
        elif (shapeName == "rectangle"):
            if (float(shapeSizes[0]) > 0 and float(shapeSizes[1]) > 0 and len(shapeSizes) == 2):
                createdShape = Rectangle(float(shapeSizes[0]), float(shapeSizes[1]))
                validShape = 1
        elif (shapeName == "triangle"):
            if (float(shapeSizes[0]) > 0 and float(shapeSizes[1]) > 0 and float(shapeSizes[2]) and len(shapeSizes) == 3):
                if (float(shapeSizes[0]) + float(shapeSizes[1]) > float(shapeSizes[2]) and float(shapeSizes[1]) + float(shapeSizes[2]) > float(shapeSizes[0]) and float(shapeSizes[2]) + float(shapeSizes[0]) > float(shapeSizes[1])):
                    createdShape = Triangle(float(shapeSizes[0]), float(shapeSizes[1]), float(shapeSizes[2]))
                    validShape = 1
    
        if (validShape == 1):
            self.shapes.append(createdShape)
        elif (validShape == 0): 
            print("\033[33mWarning : Shape is not valid\033[32m")
            self.printUsage(shapeName)
    
    def printShapes(self):
        for shape in self.shapes:
            if (shape != None):
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



