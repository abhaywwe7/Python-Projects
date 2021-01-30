# Stone-Paper-Sissor game with 10 rounds

import random
print("Welcome to Stone-Paper-Sissor Game")
can_use=["Stone", "Paper", "Sissor"]
counter=1
a=0
b=0
while counter<=10:
    print("Round ",counter)
    print("The player can only choose one of them\nStone-Paper-Sissor\n")
    player=input("Enter user choice: ")
    comp=random.choice(can_use)
    print("Computer choice: ",comp)
    if player=="Stone" and comp=="Paper":
        print("Computer wins!\n")
        b+=1;
    elif player=="Stone" and comp=="Sissor":
        print("Player wins!\n")
        a+=1
    elif player=="Paper" and comp=="Stone":
        print("Player wins!\n")
        a+=1
    elif player=="Paper" and comp=="Sissor":
        print("Computer wins!\n")
        b+=1
    elif player=="Sissor" and comp=="Stone":
        print("Computer wins!\n")
        b+=1
    elif player=="Sissor" and comp=="Paper":
        print("Player wins!\n")
        a+=1
    elif player==comp:
        print("Draw\n")
        a+=1
        b+=1
    else:
        print("Invalid User Command")
        break
    counter+=1
print("The number of rounds won by player= ",a)
print("The number of rounds won by computer= ",b)
if a>b:
    print("The game is won by Player")
elif b>a:
    print("The game is won by Computer")
else:
    print("Draw Game :(")
feedback=input("Was Game helpful [Y/N]?\n")
if feedback=="Y":
    print("Thank You for playing")

else:
    print("I hope u would love after some modifications :)")

