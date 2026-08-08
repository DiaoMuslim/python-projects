Balance = 1000
while True:
    print("===BANK MANAGEMENT SYSTEM===")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. withdraw Money")
    print("4. Exit")

    choice =input("choose an option:")

    if choice =="1":
        print("Your Balance is=",Balance)

    elif choice =="2":
        amount =float(input("Enter amount to deposit:"))
        Balance += amount    
        print("Deposit Successfully")
        print("New Balance: =",Balance)

    elif choice =="3":
        amount =float(input("Enter amount to withdraw:"))
        Balance -= amount
        print("Withdraw successfully")
        print("New Balance: =",Balance)



    elif choice =="4":
        print("Thank you for using bank management!")
        break
    else:
        print("invalid choice. try again")    