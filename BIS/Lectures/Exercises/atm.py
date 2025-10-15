print("Welcome! Please insert your card!")
counter = 0
PIN = 0

PIN = int(input("Enter PIN. You have maximum 3 tries: "))

while PIN != 1234 and counter !=2:
    counter += 1
    print(3 - counter,"tries left! ", end="")
    PIN = int(input("Enter PIN again: "))

if PIN == 1234:
    choice = 0
    while choice != 4:
        choice = int(input("Make a choice: 1, 2, 3, 4: "))
        if choice == 1:
            print("Withdraw Money.")
        elif choice == 2:
            print("New PIN")
        elif choice == 3:
            print("Consult Balance.")
        elif choice == 4:
            print("Return Card.")
        else:
            print("Wrong Choice!")
else:
    print("Card was swallowed!")