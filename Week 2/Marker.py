def menu():
    print("GRADE ASSESSOR\nF = 0-40\nD = 40-50\nC = 50-60\nB = 60-70\nA = 70-100")
    print("1) GRADER\n2) EXIT" )
    option = input("\n\nEnter Menu Option: ")
    if option == "1":
        grader()
    elif option == "2":
        quit()
    else:
        menu()

def grader():
    try:
        grade = float(input("ENTER YOUR GRADE: "))
        if grade < 0 or grade > 100:
            print("INVALID GRADE: Grade must be between 0 and 100.")
        elif grade < 40:
            print(grade, "= F")
        elif grade < 50:
            print(grade, "= D")
        elif grade < 60:
            print(grade, "= C")
        elif grade < 70:
            print(grade, "= B")
        else:
            print(grade, "= A")
    except ValueError:
        print("Invalid input. Please enter a valid numerical grade.")
    menu()

menu()