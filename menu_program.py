def menu_program():
    input_buffer = ""  # buffer to store user input
    
    while True:
        print("\n Text-Menu")
        print("1. Append data to the input buffer")
        print("2. Clear the input buffer")
        print("3. Display the input buffer")
        print("4. Exit the menu")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            data = input("Enter text for append: ")
            input_buffer += data
            print("Data appended to buffer.")
        elif choice == "2":
            input_buffer = ""
            print("Buffer cleared.")
        elif choice == "3":
            if input_buffer:
                print("Buffer is ", input_buffer)
            else:
                print("Empty Buffer")
        elif choice == "4":
            print("Exit menu")
            break
        

# Run the program
if __name__ == "__main__":
    menu_program()
