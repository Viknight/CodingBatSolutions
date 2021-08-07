def string_splosion(str):
  res=''
  for i in range(len(str)+1):
    temp=str[:i]
    res+=temp
  return res
