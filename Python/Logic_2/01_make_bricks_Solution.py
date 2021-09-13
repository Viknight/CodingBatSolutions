def make_bricks(small, big, goal):
  # all fail cases
  
  # 1. not enough bricks
  if goal > (big*5 + small):
    return False
    
  # 2. not enough small bricks(in case all big bricks cannot be used, they exceed goal)
  elif goal%5 > small:
    return False
  
  else:
    return True
  
