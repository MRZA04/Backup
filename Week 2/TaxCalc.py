import os, time
def main():
    while True:
        try:
            income = float(input("what is your annual income: "))
            break
        except ValueError:
            print("Invalid input, try again")
            time.sleep(1)
            os.system('cls')
    if income <= 12570:
        print("You don't have a tax bracket")
        print ("£",income)
    elif income >= 12571 and income < 50270:
        print ("Your tax bracket is 20%")
        taxable = income - 12570
        taxed = (taxable/100)*20
        net = taxable-taxed
        print ("Your taxed income is £",net)
    elif income >= 50271 and income < 150000:
        print ("Your tax bracket is 40%")
        taxable = income - 12570
        taxed = (income/100)*40
        net = income - taxed
        print ("Your taxed income is £",net)
    elif income >= 150000:
        print ("You have the highest taxed bracket of 45%")
        personal = income - 150000
        taxed = (personal/100)*45
        net = personal - taxed
        fnet = net + 150000
        print ("Your taxed income is £",fnet)
    Repeat()

def Repeat():
    print("Do you want to try again? (Y/N): ")
    repeat = input().lower().strip()
    if repeat == "y":
        main()
    elif repeat == "n":
        exit
    else:
        print("INVALID OPTION, TRY AGAIN")
        time.sleep(1)
        os.system('cls')
        Repeat()


main()
