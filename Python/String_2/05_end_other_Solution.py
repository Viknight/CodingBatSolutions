def end_other(a, b):
  m = a.lower()
  n = b.lower()
  return m[len(m)-len(n):] == n or n[len(n)-len(m):] == m
  
  
  # a = a.lower()
  # b = b.lower()
  # return (b.endswith(a) or a.endswith(b))
    
