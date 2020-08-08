print("This is an Armstrong number checker. Kindly input the number and we will check it for you")
message = "Your number: "


while True:
  num_list = input(message)
  # test if user wants to quit
  if num_list == 'quit':
    break
# Taking string'd input and making it into string'd LIST
  num = list(num_list)
  exp = len(num)
  add_me = 0

  for i in num:
    add_me += int(i) ** exp

  if add_me == int(num_list):
    print(num_list + " is INDEED an armstrong number!")
  else:
    print(num_list + " is NOT an armstrong number :(")
  print("When you want to quit, enter 'quit'")
