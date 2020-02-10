# This program's purpose is to determine how many square yards are in a specific surface.

width = float(input("What is the width of the room?"))
length = float(input("What is the length of the room?"))

area = length * width
area = area / 9

print("The amount of floor covering the surface is.." + str(area))
