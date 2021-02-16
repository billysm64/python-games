import random
import time

print("Tell me, the proctor, what number between 1 and 10 you want the computer to guess, and I will make the computer try and guess it. The computer gets 3 chances. But this time, the computer is more likely to win, because he got a bit smarter after doing Level 2 a bit of times.")

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

low = 1
high = 10

for tries in range(3):
    computer_guess = random.randint(low, high)
    print(f"\n\nRound {tries+1} ({3-tries} guesses remaining):\nProctor: Computer, what number is Billy thinking?")
    print(f"Computer: I pick {computer_guess}")
    if computer_guess > number_thinking:
        print(f"Proctor: Sorry, but that guess is too high.")
        high = computer_guess - 1
    elif computer_guess < number_thinking:
         print(f"Proctor: Sorry, but that guess is too low.")
         low = computer_guess + 1
    else:
        print(f"Proctor: The computer wins! Number of tries it took the computer: {tries+1}")
        exit()
    time.sleep(5)

print("The computer loses!")
