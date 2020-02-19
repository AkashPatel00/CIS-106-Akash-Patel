# This program's purpose is to determine how many square yards are in a specific surface.

def calculate_area(length, width):
    area = length * width

    return area


def calculate_surface(area):
    surface = area / 9

    return surface


def display_result(surface):
    print("The amount of floor covering the surface is.." + str(surface))


def get_length():
    print("What is the length of the room?")
    length = float(input())

    return length


def get_width():
    print("What is the width of the room?")
    width = float(input())

    return width


# Main
length = get_length()
width = get_width()
area = calculate_area(length, width)
area = calculate_surface(area)
surface = calculate_surface(area)
display_result(surface)