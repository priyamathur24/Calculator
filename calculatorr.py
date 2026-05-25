import math

# ---------------- BASIC CALCULATOR FUNCTION ---------------- #

def basic_calculator():

    print("\n--- BASIC CALCULATOR ---")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter Choice: "))

    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))

    if choice == 1:
        print("Result =", a + b)

    elif choice == 2:
        print("Result =", a - b)

    elif choice == 3:
        print("Result =", a * b)

    elif choice == 4:
        print("Result =", a / b)

    else:
        print("Invalid Choice")


# ---------------- SCIENTIFIC CALCULATOR FUNCTION ---------------- #

def scientific_calculator():

    print("\n--- SCIENTIFIC CALCULATOR ---")

    print("1. Sin")
    print("2. Cos")
    print("3. Tan")
    print("4. Log")
    print("5. Square Root")
    print("6. Power")
    print("7. Pi Value")

    choice = int(input("Enter Choice: "))

    if choice == 1:

        angle = float(input("Enter Angle: "))
        print("Result =", math.sin(math.radians(angle)))

    elif choice == 2:

        angle = float(input("Enter Angle: "))
        print("Result =", math.cos(math.radians(angle)))

    elif choice == 3:

        angle = float(input("Enter Angle: "))
        print("Result =", math.tan(math.radians(angle)))

    elif choice == 4:

        num = float(input("Enter Number: "))
        print("Result =", math.log10(num))

    elif choice == 5:

        num = float(input("Enter Number: "))
        print("Result =", math.sqrt(num))

    elif choice == 6:

        num = float(input("Enter Number: "))
        power = float(input("Enter Power: "))

        print("Result =", num ** power)

    elif choice == 7:

        print("Pi =", math.pi)

    else:
        print("Invalid Choice")


# ------ MAIN PROGRAM ------ #

print("===== CALCULATOR BY PRIYA =====")

while True:

    print("\n1. Basic Calculator")
    print("2. Scientific Calculator")
    print("3. Exit")

    main_choice = int(input("Enter Your Choice: "))

    if main_choice == 1:

        basic_calculator()

    elif main_choice == 2:

        scientific_calculator()

    elif main_choice == 3:

        print("Calculator Closed")
        break

    else:

        print("Invalid Choice")