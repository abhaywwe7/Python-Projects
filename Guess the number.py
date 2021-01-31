import random

def guessGame(a,b,actual):
    guess=int(input(f"Guess a number between {a} and {b}\n"))
    nguess=1
    while guess!=actual:
        if guess<actual:
            guess=int(input(f"Enter a bigger number: "))
            nguess+=1
        else:
            guess=int(input(f"Enter a smaller number"))
            nguess+=1
    print(f"You guessed the number in {nguess} guesses\n")
    return nguess

if __name__ == '__main__':
    a=int(input("Enter the value of a: "))
    b=int(input("Enter the value of b: "))
    actual=random.randint(a,b)
    print("\nPlayer 1 turn")
    g1=guessGame(a,b,actual)
    print("\nPlayer 2 turn")
    g2=guessGame(a,b,actual)
    if g1<g2:
        print("Player 1 won the match!")
    elif g1>g2:
        print("Player 2 won the match!")
    else:
        print("Its a tie!")
