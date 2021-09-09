def round_sum(a, b, c):
  
  l = round10(a)
  m = round10(b)
  n = round10(c)
  
  return l+m+n
  
def round10(num):
  x = num%10
  y = num//10
  
  if x < 5: return y*10
  else: return (y+1)*10
  
  
#   def round_sum(a, b, c):
#   return round10(a) + round10(b) + round10(c)
  
# def round10(num):
#   mod = num % 10
#   num -= mod
#   if mod >= 5: num += 10
#   return num