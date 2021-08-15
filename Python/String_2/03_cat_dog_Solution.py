def cat_dog(str):
  count = 0
  count1 = 0
  
  for i in range(len(str)-2):
    x = str[i:i+3]
    if x == 'cat':  count+=1
    if x == 'dog':  count1+=1
  
  if count == count1:
    return True
  else:
    return False
