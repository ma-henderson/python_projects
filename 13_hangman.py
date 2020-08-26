import requests
from random import choice
from hangman_states import HANGMANPICS as hm_list

#random word API, getting 20 'credits' of hangman game
url = 'https://random-word-api.herokuapp.com/word?number=20&swear=0'
r = requests.get(url)
print("this is the response:", str(r))

words = r.json()

# testing API returned value(s)
for word in words:
  print(word)

# INFO: this game will push the state forward after ALL players have gone
# (cont'd) However, if a player get's it right, the game ENDS
# (cont'd) Players will all see what their oponents have guessed



# Game starts here

# create player name input fn
  # Stop inputting players when 'n' or 'stop'
def players_create():
  i = 0
  input_players = []
  while True:
    temp = input("Please enter a new player's name ('n' or 'stop' to stop): ")
    if temp == 'n' or temp == 'stop':
      return input_players
    input_players.append(temp)
    print("Thank you, " + str(input_players[i] + "!"))
    i+=1

# create player dict function
def players_data(players):
  """Creates a dynamic scoreboard dict for players"""
  players_data = {}
  for name in players:
    players_data[name] = {"score": 0, "guess": '', "words": []}
  return players_data

# create variable cleanups
def var_cleanup():
  global state 
  state = -1
  global guessed_letters 
  guessed_letters = []
  global wrong_letters 
  wrong_letters = []
  global guessed_words 
  guessed_words = []
  global printed_word 
  printed_word = []
  global the_word 
  the_word = ""

# instantiate vital variables
state = -1
flag = True
game = 0
guessed_letters = []
wrong_letters = []
guessed_words = []
printed_word = []
the_word = ""
# instantiate variables for each player 
players_list = players_create()
players = players_data(players_list)


# CORE GAME LOOP:
while flag == True:
  state += 1
  if state == 0 and game > 0:
    quit_checker = input("\nWant to quit the game? Enter 'y' or 'stop': ")
    if quit_checker == 'y' or quit_checker == 'stop':
      flag == False
      break
    else:
      print("\n\n---- ///    This is round # " + str(game+1) + "     /// ----")
  # Draw state, show num of chars in word
  print(hm_list[state])
  print("\nDead man's word has " + str(len(words[game])) + " letters:\n")

  printed_word = []
  for letter in words[game]:
    # Check if letter has been guessed already
    if letter in guessed_letters:
      printed_word.append(letter)
    else:
      printed_word.append("_")
  print(the_word.join(printed_word)) #the_word remains ""
  if state > 0: 
    print("You've guessed the following CORRECT letters: " + str(guessed_letters))
    print("You've guessed the following WRONG letters: " + str(wrong_letters))
    print("You've guessed the following words: " + str(guessed_words) + "\n")

  # check if state is 2nd to last, if yes give hint
  if state == len(hm_list) - 2:
    for some_val in range(100):
      # hint = a randomly selected letter from the word
      hint = words[game][choice(range(len(words[game])))]
      # if this hint is a new letter, return it
      if hint not in guessed_letters:
        print("\nHere's a hint, the word contains the following letter: " + hint)
        break
  elif state == len(hm_list) - 1:
    print("\n#### ----- #### GAME OVER #### ----- #### ")
    print("the word was: " + words[game])
    game += 1
    var_cleanup()
    continue
  # take guesses from players
  for player, data in players.items():
    data["guess"] = input(str(player) + ", please enter your guess: ")
    
  # check if input is a single letter or word/2+
  for player, data in players.items():
    if len(data['guess']) == 1:
      # LETTER: check if letter exists in word
        if data['guess'] in words[game]:
          # TRUE: show it, POTENTIAL_BALANCE: flag state +1
          print(str(player) + ", CORRECT the letter exists in the word")
          guessed_letters.append(data['guess'])
          # FALSE: send message_wrong, next state
        else:
          print(str(player) + ", INCORRECT letter!")
          wrong_letters.append(data['guess'])

    # WORD: check if word is correct
    elif len(data['guess']) > 1: 
      if data['guess'] == words[game] and flag == True:
        # TRUE: Give player a point, reset state, flag state change
        data['score'] += 1
        data['words'].append(words[game])
        print("\n ---------- WINNER WINNER ------------\n")
        print("\t" + str(player) + " got the word right! it was: " + data['guess'])
        # create scoreboard function
        game += 1
        var_cleanup()
      # FALSE: send message_wrong, next player/state
      else:
        guessed_words.append(data['guess'])
    # ELSE: take input again
    else:
      data["guess"] = input(str(player) + ", please enter your guess: ")

# Future notes: can rotate player order to give 'fair chance' at answering first