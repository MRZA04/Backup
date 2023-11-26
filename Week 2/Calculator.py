def sqr():
    while True:
        try:
            num1 = float(input("Enter num 1: "))
            num2 = float(input("Enter num 2: "))
            sqr = (num1**2) + (num2**2)
            print(sqr)
            break
        except ValueError:
            print("Invalid input, try again")

sqr()
