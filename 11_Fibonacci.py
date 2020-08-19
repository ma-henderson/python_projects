def Fibonacho(nth_term):
  # Assupmtion of starting @ 1
  prev_num = 1
  s = 0
  for i in range(0, nth_term):
    s += prev_num
    prev_num = s - prev_num
  return s


print(Fibonacho(8))