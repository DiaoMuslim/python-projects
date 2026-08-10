print("=== unit converter ===")
print("1. meters to kilometers")
print("2. kilometers to meters")
print("3. kilograms to grams")
print("4 grams to kilograms")
print("5. celsius to fahrenheit")
print("6. fahrenheit to celsius")

choice=input("choose an option (1-6):")

if choice =="1":
    meters =float(input("enter meters:"))
    kilometers = meters / 1000
    print("Answer =",kilometers,"km")

elif choice =="2":
    kilometer =float(input("enter kilometers:"))
    meters = kilometer * 1000
    print("Answer =",meters,"meters")

elif choice =="3":
    kilograms =float(input("Enter kilograms:"))
    grams = kilograms / 1000
    print("Answer =",grams,"kg")

elif choice =="4":
    grams =float(input("Enter grams:"))
    kilograms = grams * 1000
    print("Answer =",kilograms,"g")

elif choice =="5":
    celsius =float(input("Enter celsius:"))
    fahrenheit = (celsius -32) *5/9
    print("Answer =",celsius,"c")

elif choice =="6":
    fahrenheit =float(input("Enter fahrenheit:"))
    celsius= (fahrenheit* 9/5) +32
    print("Answer =",celsius,"F")    

