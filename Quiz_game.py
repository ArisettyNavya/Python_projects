print("Welcome to Quiz!")
name = input("Please enter your name: ")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")
score = 0

answer = input("What is the keyword used to define a function in Python? ")
if answer.lower() == 'def':
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which symbol is used for single-line comments in Python? ")
if answer.lower() == '#':
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which keyword is used to create a class in Python? ").lower()
if answer == 'class':
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which keyword is used to handle exceptions in Python? ").lower()
if answer == 'try':
    print("correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + name + str(score) + " questions correct!")

print("You got " + name + str((score/4)* 100) + " %")