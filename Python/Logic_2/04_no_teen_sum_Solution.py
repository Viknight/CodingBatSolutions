def no_teen_sum(a, b, c):
  sum=0
  if 13 <= a <= 19:
    n=fix_teen(a)
    sum+=n
  else:
    sum+=a
    
  if 13 <= b <= 19:
    n=fix_teen(b)
    sum+=n
  else:
    sum+=b
    
  if 13 <= c <= 19:
    n=fix_teen(c)
    sum+=n
  else:
    sum+=c
    
  return sum 
    
def fix_teen(n):
  if n==15: 
    return 15
  elif n==16: 
    return 16
  else: 
    return 0