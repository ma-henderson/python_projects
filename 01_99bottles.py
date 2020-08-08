message1 = " bottles of beer on the wall."
message2 = " bottles of beer."

messagea = " bottle of beer on the wall."
messageb = " bottle of beer."

for num in range(100,0,-1):
  if num == 1:
    print(str(num) + messagea + "\n" + str(num) + messageb)    
  else:
    print(str(num) + message1 + "\n" + str(num) + message2)
  print("Take one down, pass it around.")
print("COMPLETE")

# message1.pop(message1.find(target)+len(target))
# target = "bottles"