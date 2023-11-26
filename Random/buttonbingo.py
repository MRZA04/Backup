import random
import tkinter as tk

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

class BingoGame:
    def __init__(self, root, size):
        self.root = root
        self.root.title(f'Bingo Game - {size}x{size} Grid')
        self.size = size
        self.removed_items = []
        self.card = self.create_card()

        self.buttons = []
        for i in range(size):
            row = []
            for j in range(size):
                btn = tk.Button(root, text="", width=60, height=8, command=lambda i=i, j=j: self.mark_item(i, j))
                btn.grid(row=i, column=j)
                row.append(btn)
            self.buttons.append(row)

        self.display_card()

    def create_card(self):
        card_items = random.sample(ITEMS, self.size * self.size)
        card = {}
        for i in range(1, self.size * self.size + 1):
            card[i] = card_items.pop()
        return card

    def display_card(self):
        for i in range(self.size):
            for j in range(self.size):
                item = self.card[i * self.size + j + 1]
                self.buttons[i][j]['text'] = item

    def mark_item(self, i, j):
        ref_num = i * self.size + j + 1
        if ref_num not in self.removed_items:
            self.removed_items.append(ref_num)
            self.buttons[i][j]['text'] = "------"

    def mainloop(self):
        self.root.mainloop()

def main_menu():
    root = tk.Tk()
    while True:
        print("\nBingo Game - Main Menu")
        print("1. 3x3 Grid")
        print("2. 4x4 Grid")
        print("3. 5x5 Grid")
        print("4. Close the program")

        choice = input("Enter your choice: ")

        if choice == "1":
            game = BingoGame(root, 3)
            game.mainloop()
        elif choice == "2":
            game = BingoGame(root, 4)
            game.mainloop()
        elif choice == "3":
            game = BingoGame(root, 5)
            game.mainloop()
        elif choice == "4":
            print("Thanks for playing!")
            root.destroy()
            break
        else:
            print("Invalid choice! Please enter a number between 1-4.")

if __name__ == "__main__":
    main_menu()