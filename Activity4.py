Player1 = input("What is your name: ")
Player2 = input("What is your name: ")

while True:
    Player1selection = input(Player1 + " Do you want Rock or Scissors or Paper: ").lower()
    Player2selection = input(Player2 + " Do you want Rock or Scissors or Paper: ").lower()
    if Player1selection == Player2selection:
       print ("its a tie")
    elif Player1selection == "rock" and Player2selection == "scissors":
        print (Player1 + " wins")
    elif Player1selection == "rock" and Player2selection == "paper":
        print (Player2 + " wins")
    elif Player1selection == "scissors" and Player2selection == "rock":
        print (Player2 + " wins")
    elif Player1selection == "scissors" and Player2selection == "paper":
        print (Player1 + " wins")
    elif Player1selection == "paper" and Player2selection == "scissors":
        print (Player2 + " wins")
    elif Player1selection == "paper" and Player2selection == "rock":
        print(Player1 + " wins")
    
    repeat = input(" do you want to play one more round? yes/no: ").lower()
    if repeat == "yes":
        pass
    else:
        raise SystemExit
