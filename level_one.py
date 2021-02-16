# Level 1: Three guesses
# Level 2: User picks a number, computer has 3 guesses
# Level 3: Computer's guesses are optimized to refine the range of guess e

import random

number_thinking = random.randint(1, 10)

tries = 0

guesses = []

print("You have to guess what number between 1 and 10 I'm thinking of. You have 3 chances, and if you can't get it after that then there's something wrong with you!")

def check_repeat(item, list, message):
    if item in list:
        print("You already guessed that one! LOLOLOL what were you thinking???")
    else:
        list.append(item)
        print(message)

for tries in range(3):
    print(f"{3-tries} attempts left.")
    guess = input("Your guess: ")
    try:
        guess = int(guess)
        if guess > 10 or guess < 1:
            print("That's not even between one and ten. Please guess a number between 1 and 10! (What an awful waste of a chance...)")
        elif guess > number_thinking:
            check_repeat(guess, guesses, "Too high")
        elif guess < number_thinking:
            check_repeat(guess, guesses, "Too low")
        elif guess == number_thinking:
            print(f"YAY you got it! You won in {tries+2} tries.")
            exit()
        else:
            print("WHAT? NO! Nooooo! o.o That's physically impossible! How could you even get to this else statement? K so like, I declare we are both in an alternate universe where math and logic themselves are inherently different. Getting to an alternate universe is a WAY bigger accomplishment than winning this stupid game. So YOU WIN!\n\nHey, by the way, go outside and make sure that you're at least in a universe where we can survive, k? Is it infested by zombies? Did you end up in the 16th century instead of now? Or did we somehow get to a universe where Teletubbies is reality, and what we previously knew as the real world is fictional? Please let me know later. Thanks.")
            exit()
    except ValueError:
        if guess == "":
            print("Please type something at all! (What an awful waste of a chance...)")
        else:
            print("You can't type something that's not a number! (What an awful waste of a chance...)")

print("You lost! How could you ever lose? YOU SUCK! It's not like this is a game of chance or anything, you know? It's all skill-based! And it's such an easy skill, to read computer minds! Anyone could do that. So you should have just won!")
