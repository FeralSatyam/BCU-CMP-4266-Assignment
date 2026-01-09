def main(contacts=[("Stish", "123"), ("Rita", "321")]):

    def menu():
        choice = input("Enter choice(v/a/d/q- to quit): ")
        match(choice):
            case 'v':
                view_contact(contacts)
            case 'a':
                add_contact(contacts)
            case 'd':
                delete_contact(contacts)
            case 'q':
                print("---------- goodbye -----------")
                exit()
            case _:
                invalid_choice()

    def view_contact(contacts):
        print("----------- view_contacts -----------")
        for i in range(len(contacts)):
            print(f"{i+1} {contacts[i][0]}: {contacts[i][1]}")
        menu()

    def add_contact(contacts):
        print("------------ add_contact -------------")
        name = input("Enter contact name: ")
        number = int(input("Enter contact number: "))
        contacts.append((name, number))
        print(f"{name} - {number} has been added into the contact.")
        menu()

    def delete_contact(contacts):
        print("------------ delete_contact --------------")
        del_index = int(input("Enter the ID of the contact to remove: "))
        contacts.pop(del_index-1)
        menu()

    def invalid_choice():
        print("----------- invalid_choice----------")
        print("Try again...")

    menu()

if __name__ == "__main__":
    main()