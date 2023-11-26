def create_list():
    my_list = []
    while True:
        user_input = input("Enter a string (type 'No' to stop): ")
        if user_input.lower() == 'no':
            break
        my_list.append(user_input)
    return my_list

def create_paragraph(my_list):
    paragraph = ' '.join(my_list)
    return paragraph

def main():
    my_list = create_list()
    paragraph = create_paragraph(my_list)
    print("This is your paragraph:")
    print(paragraph)

main()