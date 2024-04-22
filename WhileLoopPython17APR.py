
while True:
    print("Inside While loop")
    choice = input("Do you want the loop to continue? Y/N ")
    if choice in ("Y" , "y"):
        print("continuing...")
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter a 2nd number: "))

    else:
        break
          