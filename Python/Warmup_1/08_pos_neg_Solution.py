def pos_neg(a, b, negative):
  if negative==True:
    return a<0 and b<0
  else:
    if a<0:
      return b>0
    else:
      return b<0
