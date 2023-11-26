import random

ITEMS = [
    "Boris Johnson", "Cats", "Russian Wife", "C#", 
    "SQL", "Argument", "Jimmy Saville", "Daniel Craig",
    "Shitting on Apple", "Blazer", "Shitting on Tories", "Corny Joke",
    "Concern for Alfies Mental Health", "Spelling Error", "Report Networking Issue", "Air Conditioning",
    "Knee", "Flashback Moment", "Moral Compass", "Karma",
    "'Need ma Coffee'", "Distracted by some random topic", "Brexit", "Trains",
    "Snowflakes", "Complains about Racists", "Turns up late", "Forgets Name",
    "Uncomfortable Joke", "Hypocrite"
]

def create_card(size):
    card_items = random.sample(ITEMS, size*size)
    card = {}
    counter = 1
    for i in range(size):
        for j in range(size):
            card[counter] = card_items.pop()
            counter += 1
    return card

def display_card(card, size, removed_items):
    counter = 1
    for i in range(size):
        for j in range(size):
            item = card[counter]
            if len(item) < 8:
                spacing = "\t\t"
            else:
                spacing = "\t"
            print(f"{counter}. {item}", end=spacing)
            counter += 1
        print()

    print("\nRemoved items:")
    for item in removed_items:
        print(item, end=", ")
    print()

def play_game(size):
    card = create_card(size)
    removed_items = []
    while True:
        display_card(card, size, removed_items)
        try:
            ref_num = int(input(f"\nEnter the grid reference number (1-{size*size}) to mark an item or '0' to go back to main menu: "))
            if ref_num == 0:
                return
            if 1 <= ref_num <= size*size:
                removed_items.append(card[ref_num])
                card[ref_num] = "------"
            else:
                print("Invalid reference number!")
        except ValueError:
            print("Please enter a valid number!")

def main_menu():
    while True:
        print("\nBingo Game - Main Menu")
        print("1. 3x3 Grid")
        print("2. 4x4 Grid")
        print("3. 5x5 Grid")
        print("4. Close the program")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            play_game(3)
        elif choice == "2":
            play_game(4)
        elif choice == "3":
            play_game(5)
        elif choice == "4":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-4.")


main_menu()