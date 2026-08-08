while True:
    print("\n===Expense Tracker===")
    print("1. calculate Expence")
    print("2.exit")

    choice =input("choose your choice:")

    if choice =="1":
        income =float(input("Enter your income:,GHC"))

        Food =float(input("food expense: GHC"))
        Transport =float(input("Enter your Transport expense: GHC"))
        Rent =float(input("Enter your Rent exense:"))
        Electricity =float(input("Enter Electricity expense"))
        Other =float(input("Enter other expense:"))

        total = Food + Transport + Rent + Electricity + Other
        balance = income - total

        print("\n-----Summary-----")
        print("income: GHC =",income)
        print("toyal expense: GHC =",total)
        print("Remaining balance: GHC =",balance)

        if balance == 0:
            print("Great! You saved your money")
        elif balance == 0:
            print("You spent all your money")
        else:
            print("Warning! You spent more than your income")    
            
    elif choice =="2":
        print("Thank you for using expense tracker")
        break

    else:
        print("invalid choice.try again")

