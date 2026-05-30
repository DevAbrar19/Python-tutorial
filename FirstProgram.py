import random

randNum = random.randint(1, 100)

while True:
    num = int(input("Enter a number: "))

    if(num == randNum):
        print("Congratulations! You guessed the correct number.")
        break
    elif(num > randNum):
        print("You have guessed a larger number. ")
    else:
        print("You have guessed a smaller number.")

print("Game Over.")