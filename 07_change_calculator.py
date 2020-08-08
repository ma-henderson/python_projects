from math import floor

# Core info
coins = {
  'quarter': 0.25,
  'dime': 0.10,
  'nickel': 0.05,
  'penny': 0.01
}
# below should be in qty
coins_returned = {}

# FORMATTING FOR TESTS
testing_clear = '\n-----------------------------------\n'
print(testing_clear)

# Messages
message_welcome = "Welcome to the change calculator!\n"
message_cost = "What is the total cost of the products?\nTotal: "
message_amount = "What is the amount being paid to you?\nAmount: "
message_end = "\nYou need to pay the customer the following coins:\n"


def exiter(string):
  string = string.lower()
  if string == "q" or string == "quit":
    print("quiting...")
    return True


# take and store value
while True:
  input_cost = input(message_cost)
  if exiter(input_cost):
    break
  input_amount = input(message_amount)
  if exiter(input_amount):
    break
  cost = float(input_cost)
  amount = float(input_amount)

  # calculate change from inputs
  change = amount - cost
  if change < 0:
    print("## -- ## NOT ENOUGH PAYMENT ## -- ## ")
    print(testing_clear)
    continue
  elif change == 0:
    print("No change needed!")
    continue

  round(change, 2)
  # check per denomination
    # from largest to smallest - coins is conveniently built that way
  for coin in coins:
    # if largest % > 0
    if change > 0:
      if change >= coins[coin]:
        
        # check how many fit without overloading and without overpay
        on_hand = floor(change / coins[coin])
        coins_returned[coin] = on_hand
        
        # add item and qty to returned var (dict)
        change -= on_hand * coins[coin]
        change = round(change, 2)
        

  # print result
  print(message_end)
  for coin in coins_returned:
    if coin != 'penny':
      print(str(coins_returned[coin]) + " " + coin.title() + "(s)")
    else:
      print(str(coins_returned[coin]) + " Pennies")

  # print("coin dictionary return:  " + str(coins_returned))
  # print("change at end:  " + str(change))
  print(testing_clear)
