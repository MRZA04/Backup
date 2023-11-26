def create_list():    
    integers = []
    while True:
        print("Add number to your list, type end to finish: ")
        user_input = input()
        if user_input == "end":
            break
        try:
            user_input = int(user_input)
            integers.append(int(user_input))
        except ValueError:
            print("INVALID INPUT")
            main()
    return integers

def sum_of_list(integers):
    sum_list = sum(integers)
    return sum_list

def main():
    integers = create_list()
    sum_list = sum_of_list(integers)
    print("The sum of your list is:", sum_list)

main()