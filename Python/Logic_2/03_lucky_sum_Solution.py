def lucky_sum(a, b, c):
  total=0
  
  if a!=13:
    total+=a
    if b!=13:
      total+=b
      if c!=13:
        total+=c
  return total
