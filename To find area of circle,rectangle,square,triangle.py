import math

def area_circle(radius):
  area = math.pi * radius * radius
  return area

def area_rectangle(length, width):
  area = length * width
  return area

def area_square(side):
  area = side * side
  return area


def area_triangle(base, height):
  area = 0.5 * base * height
  return area

shape = input("Enter the shape name: ")


if shape == "circle":
  radius = float(input("Enter the radius: "))
  area = area_circle(radius)
  print(f"The area of the circle is {area:.2f}")


elif shape == "rectangle":
  length = float(input("Enter the length: "))
  width = float(input("Enter the width: "))
  area = area_rectangle(length, width)

  print(f"The area of the rectangle is {area:.2f}")


elif shape == "square":
  side = float(input("Enter the side: "))
  area = area_square(side)
  
  print(f"The area of the square is {area:.2f}")


elif shape == "triangle":
  base = float(input("Enter the base: "))
  height = float(input("Enter the height: "))
  area = area_triangle(base, height)

  print(f"The area of the triangle is {area:.2f}")


else:
  print("Invalid shape name")
