# importing libraries

import random
import playsound
from playsound import playsound

#How many times you want to play

Turn=int(input("Enter the number of turns you want to play:"))

#options that are available
options = ["rock", "paper", "scissor"]

yourscore = 0
computerscore = 0

for i in range(1,Turn+1):
    # computer random input
    computer_input = random.choice(options)

    #user input
    User_input = str(input()).lower()

    if ((User_input == "rock") and (computer_input=="scissor")):
        print("You Won this round")
        yourscore = yourscore + 1
        playsound("C://Users//gokul//Downloads//Mario-coin-sound.mp3")

    elif ((User_input == "paper") and (computer_input=="rock")):
        print("You Won this round")
        yourscore = yourscore + 1
        playsound("C://Users//gokul//Downloads//Mario-coin-sound.mp3")

    elif ((User_input == "scissor") and (computer_input=="paper")):
        print("You Won this round")
        yourscore = yourscore + 1
        playsound("C://Users//gokul//Downloads//Mario-coin-sound.mp3")

    elif ((User_input!=computer_input)):
        print("ERROR")

    elif (User_input==computer_input):
        print("draw")

    else:
        print("Computer Won this round")
        computerscore=computerscore+1
        playsound("C://Users//gokul//Downloads//Mario-coin-sound.mp3")

print("User score:",yourscore)
print("Computer score:",computerscore)

if yourscore>computerscore:
    print("This game is won by the User")

elif yourscore==computerscore:
    print("the match is draw")

else:
    print("this game is won by the Computer")