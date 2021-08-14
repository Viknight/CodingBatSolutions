def string_match(a, b):
  count=0
  
  for i in range(len(b)-1):
    x=a[i:i+2]
    y=b[i:i+2]
    if x==y:
      count+=1
  return count
