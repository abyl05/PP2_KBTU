from phonebook import *

while True:
    print("""
1. Add contact
2. Search
3. Filter by group
4. Sort
5. Export JSON
6. Import JSON
0. Exit
""")

    choice = input("> ")

    if choice == "1":
        add_contact(
            input("name: "),
            input("email: "),
            input("birthday YYYY-MM-DD: "),
            input("group id: ")
        )

    elif choice == "2":
        search(input("query: "))

    elif choice == "3":
        filter_by_group(input("group: "))

    elif choice == "4":
        sort_contacts(input("name/birthday: "))

    elif choice == "5":
        export_json()

    elif choice == "6":
        import_json()

    elif choice == "0":
        break