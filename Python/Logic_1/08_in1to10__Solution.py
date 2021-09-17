def in1to10(n, outside_mode):
  if outside_mode:
    return n<=1 or 10<=n
  else:
    return 1 <= n <= 10
