def last2(str):
  a=str[len(str)-2:]
  count=0
  for i in range(len(str)-2):
    sub=str[i:i+2]
    if a==sub:
      count+=1
  return count
