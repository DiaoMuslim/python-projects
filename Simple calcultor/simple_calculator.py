print("==simple calcuator===")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")

choice = input("choose an operation (1-4):")

num1 =float(input("Enter the first number:"))
num2 =float(input("Enter the second number:"))

if choice =="1":
    print("Answer =", num1 + num2)

elif choice =="2":
    print("Answer =", num1 - num2)

elif choice =="3":
    print("Answer =", num1 * num2)

elif choice =="4":
    if num2 ==0:
        print("Error: You cannot devide by zero.")
    else:
        print("Answer =", num1 / num2)

else:
    print("invalid choice")               
