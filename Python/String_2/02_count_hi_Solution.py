def count_hi(str):
  count=0
  for i in range(len(str)-1):
    x = str[i:i+2]
    if x == 'hi':
      count+=1
  return count
    
