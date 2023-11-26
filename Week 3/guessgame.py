import os
import random
def main():
    ranum = random.randint(0,9)
    while True:
        userguess = input("GUESS THE NUMBER BETWEEN 1-9 (EXIT to end game):")
        if userguess.lower().strip() == "exit":
            break
        try:
            userguess = int(userguess)
        except ValueError:
            print("Please enter a valid number or 'exit'.")
            continue
        if userguess == ranum:
            print ("CONGRATS YOU GOT IT RIGHT")
            quit()
        elif  userguess < ranum:
            print("HIGHER, TRY AGAIN")
            continue
        elif  userguess > ranum:
            print("LOWER, TRY AGAIN")
            continue
        else:
            print("INVALID NUMBER, RESTARTING")
            main()
main()    