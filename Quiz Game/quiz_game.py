("===PYTHON QUIZ GAME===")
score = 0

print("\nQuestion 1")
print("what is the output of (1 + 3)?")
print("a. 23")
print("b. 5")
print("c. 6")
print("d. Error")
Answer =input("Your Answer:").lower()


if  Answer =="b":
    print("correct")
    score += 1
else:
    print("wrong!the correct answer is b")

print("\nQuestion 2")
print("which keyboard is use to create a loop?")
print("a. if")
print("b. for")
print("c. print")
print("d. input")
Answer =input("Your Answer:").lower()

if Answer =="a":
    print("correct")
    score += 1
else:
    print("wrong! the correct answer is a")

print("\Question 3")
print("Which of the following is used to represent an Algorithm graphically")
print("a. Browser")
print("b. Database")
print("c. Flowchart")
print("d. Spreadsheet")
Answer =input("Your Answer:").lower()

if Answer =="c":
    print("correct")
    score += 1
else:
    print("wrong! the correct answer is c")

print("\nQuestion 4")
print("which of the following is a type of RAM?")
print("a. DDR5")
print("b. DVD")
print("c. SSD")
print("d. BIOS")
Answer=input("Your Answer:").lower()

if Answer =="a":
    print("Correct")
    score += 1
else:
    print("wrong!the correct answer is a")
    
print("\nQuestion 5")
print("which of the following is a primitive data structure")
print("a. Stack")
print("b. queue")
print("c. Array")
print("d. Integer")
Answer =input("Your Answer:").lower

if Answer =="d":
    print("Correct")
    score += 1
else:
    print("wrong!Your correct answer is d")

("\n===Quize Finished===")
print("your score is =",score,"out of 3")
if score == 3:
    print("Excellent!")
elif score == 2:
    print("Good job!")
else:
    print("keep practicing")            
