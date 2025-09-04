# Program Name: textmenu.py 
# Course: IT3883/Section W02
# Student Name: Anthony Giso
# Assignment Number: 1
# Due Date: 09/05/ 2025
# Purpose: a python program that implements a text-based menu. 
# Used Python module and chapters.

#Defines main 
def textmenu():
    input_buffer = ""  # buffer to store user input
    #loop until exit
    while True:
        
        print("\n Text-Menu")
        print("1. Append data to the input buffer")
        print("2. Clear the input buffer")
        print("3. Display the input buffer")
        print("4. Exit the menu")
#printing options for menu
        choice = input("Enter choice from menu. ")

        if choice == "1":
            data = input("Enter text for append: ") #input from user
            input_buffer += data      #adding to buffer
            print("Data appended for buffer.")
        elif choice == "2":
            #reset string
            input_buffer = ""
            print("Buffer cleared.")
        elif choice == "3":
            if input_buffer:
                print("Buffer is ", input_buffer)
            else:
                print("Empty Buffer")
        elif choice == "4":
            print("Exit menu")
            break  #stop 
        

# run
if __name__ == "__main__":
    textmenu()
