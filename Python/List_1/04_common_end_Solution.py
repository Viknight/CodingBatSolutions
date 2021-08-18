def common_end(a, b):
  return (a[:1] == b[:1]) or (a[len(a)-1] == b[len(b)-1])
