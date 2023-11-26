import os
import time
visited_cities = []

def add_city():
    city = input("Enter the name of the city you visited: ")
    visited_cities.append(city)
    print(f"{city} has been added to your list of visited cities.")


def view_cities():
    if visited_cities:
        print("List of Visited Cities:")
        print(visited_cities)
        end = input("Press enter to return to Main Menu: ")
        if end == "":
            return
        else:
            return
    else:
        print("You haven't visited any cities yet.")

def remove_city():
    view_cities()
    if visited_cities:
        try:
            index_to_remove = int(input("Enter the number of the city to remove: ")) - 1
            if 0 <= index_to_remove < len(visited_cities):
                removed_city = visited_cities.pop(index_to_remove)
                print(f"{removed_city} has been removed from your list of visited cities.")

            else:
                print("Invalid input. Please enter a valid city number.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    else:
        print("Your list of visited cities is empty, nothing to remove.")


while True:
    time.sleep(2)
    os.system('cls')
    print("\nOptions:")
    print("1. Add a city to the list")
    print("2. View the list of visited cities")
    print("3. Remove a city from the list")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        time.sleep(2)
        os.system('cls')
        add_city()
    elif choice == '2':
        time.sleep(2)
        os.system('cls')
        view_cities()
    elif choice == '3':
        time.sleep(2)
        os.system('cls')
        remove_city()
    elif choice == '4':
        time.sleep(2)
        print("Exiting the program. Goodbye!")
        break
    else:
        time.sleep(2)
        os.system('cls')
        print("Invalid choice. Please enter a valid option (1/2/3/4).")