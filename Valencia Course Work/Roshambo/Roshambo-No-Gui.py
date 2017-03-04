import random

print("----------------------------------------------\n"
      "_.-*'*-.__.-*'*-._ Roshambo _.-*'*-.__.-*'*-._\n"
      "----------------------------------------------\n")

def play():
    print("----------------------------------------------")
    print("What's your play?")
    playerChoices = [0, 0]
    i = 0
    while i < 2:
        print("Hand #{}".format(i + 1))
        playerChoices[i] = int(input("Rock (1), Paper (2), or Scissors (3)?\n"))
        i += 1
    opponentChoices = [random.randint(1, 3), random.randint(1, 3)]

    i = 0
    for choice in playerChoices:
        if playerChoices[i] == opponentChoices[i]:
            print("You both chose the same thing for Hand #{}.".format(i + 1))
            print("It's a draw!\n")
        else:
            if playerChoices[i] == 1:
                if opponentChoices[i] == 3:
                    print("Opponent chose Scissors.")
                    print("Hand #{} Won!\n".format(i + 1))
                else:
                    print("Opponent chose Paper.")
                    print("Sorry, Hand #{} Lost!\n".format(i + 1))
            elif playerChoices[i] == 2:
                if opponentChoices[i] == 1:
                    print("Opponent chose Rock.")
                    print("Hand #{} Won!\n".format(i + 1))
                else:
                    print("Opponent chose Scissors")
                    print("Sorry, Hand #{} Lost!\n".format(i + 1))
            elif playerChoices[i] == 3:
                if opponentChoices[i] == 2:
                    print("Opponent chose Paper")
                    print("Hand #{} Won!\n".format(i + 1))
                else:
                    print("Opponent chose Rock.")
                    print("Sorry, Hand #{} Lost!\n".format(i + 1))
        i += 1

# Get user input.
while True:
    play()






