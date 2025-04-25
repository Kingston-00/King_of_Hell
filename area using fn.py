def area_rectangle(length, breadth):
    return length * breadth

def area_triangle(base, height):
    return 0.5 * base * height

def area_square(side):
    return side * side

# Rectangle
l = float(input("Enter length of rectangle: "))
b = float(input("Enter breadth of rectangle: "))
print("Area of rectangle:", area_rectangle(l, b))

# Triangle
base = float(input("\nEnter base of triangle: "))
height = float(input("Enter height of triangle: "))
print("Area of triangle:", area_triangle(base, height))

# Square
side = float(input("\nEnter side of square: "))
print("Area of square:", area_square(side))
