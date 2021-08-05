def front_times(str, n):
  front_end=3
  if len(str)<3:
    front_end=len(str)
    
  front=str[:front_end]
  return front*n
