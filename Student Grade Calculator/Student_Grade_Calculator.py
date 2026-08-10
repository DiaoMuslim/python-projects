print("===Student Grade Calculator ===" )

score = float(input("Enter your score:"))
if score < 0 or score > 100:
    print("error: scre must be between 0 and 100.")
else:
   
    if score >= 80:
        print("Grade: A")

    elif score >= 70:
        print("Grade: B")

    elif score >= 60:
        print("Grade: C")

    elif score >= 50:
        print("Grade: D")

    else:
        print("Grade: F")                
