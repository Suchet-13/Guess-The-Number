import random
num = random.randint(1,9)
guess = int(raw_input("Enter any number from 1 to 9: "))
while n != "guess":
    print
    if guess < num:
        print("Guess is too low, choose a higher number")
        guess = int(raw_input("Enter any number from 1 to 9: "))

    elif guess > num:
        print("Guess is too high, choose another number")
        guess = int(raw_input("Enter any number from 1 to 9: "))

    else:
        print("You guessed correctly!")
        break
    print