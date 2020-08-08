# import random
#print(random.randrange(3))

# test if 'break' breaks all loops or current one -> current one
# for number in range(5,10):
#   print(number)
#   for num in range(0,5):
#     if num == 3:
#       print("Exiting")
#       break 
#     else:
#       print(num)

# choice_alternatives = ['r', 'rock', 'p', 'paper', 's', 'scissors']
# choice_player = input('your choice: ')
# def choice_checker(choice, alternatives):
#   """Checks if the user's input is OK, does not stop until OK"""
#   while True:
#     for num in range(0, len(alternatives)):
#       if choice == alternatives[num]:
#         return choice
#     print("Incorrect input, please select one of the following:" + str(alternatives))
#     choice = input("Your choice: ")

# new_choice = choice_checker(choice_player, choice_alternatives)
# print(new_choice)

choice_player_ok = 'r'
if choice_player_ok == 'r' or 'rock':
  choice_player_ok = 0
print(choice_player_ok)