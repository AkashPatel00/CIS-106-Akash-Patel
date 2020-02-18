# This program's purpose is to determine how many square yards are in a specific surface.

def calculateArea(length, width):
    area = length * width

    return area


def calculateSurface(area):
    surface = area / 9

    return surface


def displayResult(surface):
    print("The amount of floor covering the surface is.." + str(surface))


def getLength():
    print("What is the length of the room?")
    length = float(input())

    return length


def getWidth():
    print("What is the width of the room?")
    width = float(input())

    return width


# Main
length = getLength()
width = getWidth()
area = calculateArea(length, width)
area = calculateSurface(area)
surface = calculateSurface(area)
displayResult(surface)