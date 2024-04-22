num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))
choice = input("Enter operation (a for addition, s for subtraction): ")

if choice == 'a':
    print (num1 * num2)
elif choice == 's' :
     print (num1 / num2)
elif choice == 'A' :
    print (num1 * num2)
elif choice == 's' :
     print (num1 / num2)
elif choice == 'w' :
    print("Invalid option!")
    