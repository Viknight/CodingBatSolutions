def lone_sum(a, b, c):
  total=0
  if a==b:
    if b==c:
      return 0
    else:
      return c
  
  elif a==c:
    if b==c:
      return 0
    else:
      return b
  
  else:
    if b!=c:
      return a+b+c
    else:
      return a


# #sum = 0
#   if a != b and a != c: sum += a
#   if b != a and b != c: sum += b
#   if c != a and c != b: sum += c
  
#   return sum