shopping_list = ["apple", "chocolate", "coffee", "milk", "cake", "mint"]

while True:
    print("===== Shopping Manager =====")
    print("1. Show shopping list")
    print("2. Add item")
    print("3. Remove item")
    print("4. Search item")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":

        for item in shopping_list:
            print(item)

    elif choice == "2":

       new_item = input("Enter item: ")
       shopping_list.append(new_item)
       print(f"{new_item} added!")

    elif choice == "3":

        item = input("Enter item to remove: ")
        shopping_list.remove(item)
        print(f"{item} removed!")

    elif choice == "4":
        
        item = input("Enter item to search: ")

        if item in shopping_list:
            print(f"{item} is in your shopping list!")
        else:
            print(f"{item} is not in your shopping list.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option!")