import math
import turtle

def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height


def parallelogram_area(base, height):
    return base * height


def rectangle_area(length, width):
    return length * width


def square_area(side):
    return side * side


def triangle_area(base, height):
    return 0.5 * base * height


def circle_area(radius):
    return math.pi * radius * radius


def draw_trapezoid(base1, base2, height):
    if base1 < base2:
        base1, base2 = base2, base1

    if (base1 - base2) / 2 < height:
        print("Given dimensions can't form a valid trapezoid.")
        return

    angle = math.degrees(math.atan(height / ((base1 - base2) / 2)))
    turtle.forward(base1)
    turtle.left(180 - angle)
    turtle.forward(height / math.sin(math.radians(angle)))
    turtle.left(angle)
    turtle.forward(base2)
    turtle.left(180 - angle)
    turtle.forward(height / math.sin(math.radians(angle)))
    

def draw_parallelogram(base, height):
    angle = math.degrees(math.atan(height/base))
    
    turtle.forward(base)
    turtle.left(90 + angle)
    turtle.forward(height)
    turtle.left(90 - angle)
    turtle.forward(base)
    turtle.left(90 + angle)
    turtle.forward(height)
    turtle.left(90 - angle)
    

def draw_rectangle(length, width):
    for _ in range(2):
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
        

def draw_square(side):
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)
        

def draw_triangle(base, height):
    side = math.sqrt(height**2 + (base / 2)**2)
    angle1 = math.degrees(math.asin(height / side))
    angle2 = 180 - 2 * angle1
    turtle.forward(base)
    turtle.left(180 - angle1)
    turtle.forward(side)
    turtle.left(180 - angle2)
    turtle.forward(side)
    

def draw_circle(radius):
    turtle.circle(radius)


def mainMenu():
    print("Choose a shape:")
    print("1. Trapezoid")
    print("2. Parallelogram")
    print("3. Rectangle")
    print("4. Square")
    print("5. Triangle")
    print("6. Circle")

    choice = int(input())

    if choice == 1:
        base1 = float(input("Enter base1 of the trapezoid: "))
        base2 = float(input("Enter base2 of the trapezoid: "))
        height = float(input("Enter height of the trapezoid: "))
        print(f"Area of the trapezoid: {trapezoid_area(base1, base2, height)}")

        if (abs(base1 - base2) / 2) >= height:
            draw_trapezoid(base1, base2, height)
        else:
            print("Given dimensions can't form a valid trapezoid.")

    elif choice == 2:
        base = float(input("Enter base of the parallelogram: "))
        height = float(input("Enter height of the parallelogram: "))
        print(f"Area of the parallelogram: {parallelogram_area(base, height)}")
        draw_parallelogram(base, height)

    elif choice == 3:
        length = float(input("Enter Length of the Rectangle: "))
        width = float(input("Enter Width of the Rectangle: "))
        print(f"Area of the Rectangle: {rectangle_area(length, width)}")
        draw_rectangle(length, width)

    elif choice == 4:
        side = float(input("Enter Side of the Square: "))
        print(f"Area of the Square: {square_area(side)}")
        draw_square(side)

    elif choice == 5:
        base = float(input("Enter Base of the Triangle: "))
        height = float(input("Enter Height of the Triangle: "))
        print(f"Area of the Triangle: {triangle_area(base, height)}")
        draw_triangle(base, height)

    elif choice == 6:
        radius = float(input("Enter Radius of the Circle: "))
        print(f"Area of the Circle: {circle_area(radius)}")
        draw_circle(radius)

    else:
        print("Invalid choice!")
        
    turtle.exitonclick()
    anykey=input("\nEnter anything to return to main menu...\n\n\n")
    mainMenu()
    

mainMenu()