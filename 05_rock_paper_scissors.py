import random
message_welcome = "Welcome to the Rock Paper Scissors Game!"
message_name = "Please input your name!"
message_choice = "Select one of the following:\n- R or Rock\n- P or Paper\n- S or Scissors"
message_win = "You WON!"
message_loss = "You LOST :("
message_end = "If you'd like to quit, enter 'q' or 'quit'"
message_quit = "quitting..."
choice_alternatives = ['r', 'rock', 'p', 'paper', 's', 'scissors']


# Functions:
def choice_checker(choice, alternatives):
  """Checks if the user's input is OK, does not stop until OK"""
  while True:
    for num in range(0, len(alternatives)):
      if choice == alternatives[num]:
        return choice
    print("Incorrect input, please select one of the following:" + str(alternatives))
    choice = input("Your choice (lowercase only): ")

#new_choice = choice_checker(choice_player, choice_alternatives)

# Player starts game, is welcomed
print(message_welcome)
print(message_name)
# Player inputs name
name = input("Your name: ")
while True:
  # Player is asked what choice he would like to make
  print(message_choice)
  # Input is Checked and stored
  choice_player = input("Your choice: ")
  if choice_player == 'q' or choice_player == 'quit':
    print(message_quit)
    break
  choice_player_ok = choice_checker(choice_player, choice_alternatives)
  # Player choice is converted to number
  if choice_player_ok == 'r' or choice_player_ok == 'rock':
    choice_player_num = 0
  elif choice_player_ok == 'p' or choice_player_ok == 'paper':
    choice_player_num = 1
  elif choice_player_ok == 's' or choice_player_ok == 'scissors':
    choice_player_num = 2
  # Computer randomizes its choice
  choice_comp = random.randrange(3)
  # Comparison is made
  if choice_comp == 2 and choice_player_num == 1:
    decision = 0
  elif choice_comp == 1 and choice_player_num == 0:
    decision = 0
  elif choice_comp == 0 and choice_player_num == 2:
    decision = 0
  else:
    decision = 1
  # winner declared and printed
  if decision == 1:
    print(message_win)
  else:
    print(message_loss)
  # score is recorded and printed
  # player decides if he continues playing (q or quit)
  print("\n" + message_end)

#BONUS: if player's name is "Tom" or "Tomas", Player always loses
  # Note, if extra time use REGEXP to detect variations of tom