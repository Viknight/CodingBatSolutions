def make_chocolate(small, big, goal):
  big *= 5
  
  if big + small < goal or goal%5 > small:
    return -1
  else:
    small = goal - big
    return small%5 if small < 0 else small 
