print("Welcome to Rock, Paper, Scissors!")
print()
print("Select your move (R, P or S)")
print()
player1Move = input("Player 1 > ")
print()
player2Move = input("Player 2 > ")
print()
if player1Move == "R" or player1Move =="r":
  if player2Move=="R" or player2Move =="r":
    print("You both picked Rock! It's a draw!")
  elif player2Move == "S" or player2Move == "s":
    print("Player1 wins over Player2's Scissors with their rock!")
  elif player2Move=="P" or player2Move =="p":
    print("Player1's Rock loses against Player2's Paper!")
  else:
    print("Invalid Move, Player 2!")
elif player1Move=="P"or player1Move == "p":
  if player2Move=="R" or player2Move =="r":
    print("Player1's Paper wins over Player2's rock!")
  elif player2Move=="S" or player2Move =="s":
    print("Player1's Paper is ruined by Player2's Scissors!")
  elif player2Move=="P" or player2Move == "p":
    print("You both chose paper! It's a draw!")
  else:
    print("Invalid Move Player 2!")
elif player1Move=="S" or player1Move =="s":
  if player2Move=="R" or player2Move =="r":
    print("Player 2's Rock wins over Player1's Scissors")
  elif player2Move=="S" or player2Move == "s":
    print("You both chose scissors! It's a draw!")
  elif player2Move=="P" or player2Move == "p":
    print("Player1's Scissors wins over Player2's paper!")
  else:
    print("Invalid Move Player 2!")
else:
  print("Invalid Move Player 1!")
