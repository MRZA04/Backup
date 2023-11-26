# Define a function to check if the user wants to continue
def check_continue():
    while True:
        choice = input("Do you want to continue (Y/N)? ").strip().lower()
        if choice == 'n':
            return False
        elif choice == 'y':
            return True
        else:
            print("Please enter 'Y' for Yes or 'N' for No.")

# Define a function to check if the input is numeric and convert it to int
def check_numeric(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid numeric value.")

# Define a function to compute the pay
def computepay(hours, rate=10):
    if hours <= 40:
        return hours * rate
    else:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * (rate * 1.5)
        return regular_pay + overtime_pay

# Main program
print("Welcome to the Pay Computation Program")
continue_flag = True

while continue_flag:
    hours = check_numeric("Enter the number of working hours: ")
    rate_input = input("Enter the hourly rate (optional, press Enter to use the default rate of £10): ").strip()

    if rate_input:
        rate = float(rate_input)
    else:
        rate = 10

    pay = computepay(hours, rate)
    print(f"Pay: £{pay:.2f}")

    continue_flag = check_continue()

print("Thank you for using the Pay Computation Program. Goodbye!")