def main():
    print ("SCORE ORGANISER")

    scores = []

    while True:
        inp = input("Enter score or (done) to finish, (quit) to end the program): ")

        if inp.lower().strip() == "done":
            if len(scores) == 0:
                print("No marks were entered.")
            else:
                print("Largest mark:", max(scores))
                print("Smallest mark:", min(scores))
                print("Average mark:", sum(scores) / len(scores))
            break
        elif inp.lower() == "quit":
            print("ENDING PROGRAM")
            break
        else:
            try:
                score = float(inp)
                scores.append(score)
            except ValueError:
                print("Invalid input. Please enter a valid number or 'done' to finish.")

main()