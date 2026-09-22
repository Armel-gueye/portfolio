"""Command-line shopping list program that lets the user edit a shopping list."""

items = []  # Initialize an empty list

while True:  # Main program loop

    try:
        choice = int(
            input(
                "_______________________________________________________________________________\n"
                "Choose one of the following 5 options:\n"
                "1: Add an item to the list\n"
                "2: Remove an item from the list\n"
                "3: Display the list\n"
                "4: Clear the list\n"
                "5: Quit\n"
                "Your choice: "
            )
        )
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 5.")
        continue

    if choice == 1:  # Add an item
        item_to_add = input("Enter the item to add: ")
        items.append(item_to_add)
        print(f"{item_to_add} was added to the list.")

    elif choice == 2:  # Remove an item
        item_to_remove = input("Enter the item to remove: ")

        if item_to_remove in items:
            items.remove(item_to_remove)
            print(f"{item_to_remove} was removed from the list.")
        else:
            print("This item is not in the list. Please try again.")
            continue

    elif choice == 3:  # Display the list
        print(f"Current shopping list:\n{items}")

    elif choice == 4:  # Clear the list
        items.clear()
        print("The list was cleared successfully.")

    elif choice == 5:  # Exit the loop
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
        continue
