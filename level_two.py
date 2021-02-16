# Level 1: Three guesses
# Level 2: User picks a number, computer has 3 guesses
# Level 3: Computer's guesses are optimized to refine the range of guess e

import random
import time

print("Tell me, the proctor, what number between 1 and 10 you want the computer to guess, and I will make the computer try and guess it. The computer gets 3 chances.")

frustration_level = 0

while 1:
    number_thinking = input("Proctor: What number are you thinking of? ")
    try:
        number_thinking = int(number_thinking)
        if number_thinking > 10 or number_thinking < 1:
            print("ERROR: I said a number between 1 and 10!")
        else:
            print("Proctor: Alrighty, here we go!")
            break
    except ValueError:
        if number_thinking == "":
            print("ERROR: Don't just type nothing!")
        else:
            print("ERROR: WHY DID YOU PUT SOMETHING THAT'S NOT A NUMBER?")
    frustration_level +=1
    if frustration_level == 5:
        while 1:
            try:
                print("\n\nAlright, that's it! You turd! I'm filling up your terminal with garbage because you just won't stop being mean to me!\n\n")
            except KeyboardInterrupt:
                for i in range(10000):
                    print("Nice try! But YOU CAN'T ESCAPE MY WRATH ya joik!")

guesses = []


for tries in range(3):
    computer_guess = random.randint(1, 10)
    print(f"\n\nRound {tries+1} ({3-tries} guesses remaining):\nProctor: Computer, what number is Billy thinking?")
    print(f"Computer: I pick {computer_guess}")
    if computer_guess == number_thinking:
        print(f"Proctor: The computer wins! Number of tries it took the computer: {tries+2}")
        exit()
    else:
        if computer_guess in guesses:
            print("Proctor: You already guessed that one! LOLOLOL what were you thinking???")
        else:
            print("Proctor: Nah, that's wrong.")
            guesses.append(computer_guess)
    time.sleep(5)

print("The computer loses!")

#

# def check_repeat(item, list, message):
#     if item in list:
#         print("You already guessed that one! LOLOLOL what were you thinking???")
#     else:
#         list.append(item)
#         print(message)
#
# for tries in range(3):
#     print(f"{3-tries} attempts left.")
#     try:
#         guess = int(guess)
#         if guess > 10 or guess < 1:
#             print("That's not even between one and ten. Please guess a number between 1 and 10! (What an awful waste of a chance...)")
#         elif guess > number_thinking:
#             check_repeat(guess, guesses, "Too high")
#         elif guess < number_thinking:
#             check_repeat(guess, guesses, "Too low")
#         elif guess == number_thinking:
#             print(f"YAY you got it! You won in {tries+1} tries.")
#             exit()
#         else:
#             print("WHAT? NO! Nooooo! o.o That's physically impossible! How could you even get to this else statement? K so like, I declare we are both in an alternate universe where math and logic themselves are inherently different. Getting to an alternate universe is a WAY bigger accomplishment than winning this stupid game. So YOU WIN!\n\nHey, by the way, go outside and make sure that you're at least in a universe where we can survive, k? Is it infested by zombies? Did you end up in the 16th century instead of now? Or did we somehow get to a universe where Teletubbies is reality, and what we previously knew as the real world is fictional? Please let me know later. Thanks.")
#             exit()
#     except ValueError:
#         if guess == "":
#             print("Please type something at all! (What an awful waste of a chance...)")
#         else:
#             print("You can't type something that's not a number! (What an awful waste of a chance...)")
#
# print("You lost! How could you ever lose? YOU SUCK! It's not like this is a game of chance or anything, you know? It's all skill-based! And it's such an easy skill, to read computer minds! Anyone could do that. So you should have just won!")
