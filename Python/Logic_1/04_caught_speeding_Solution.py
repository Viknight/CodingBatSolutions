def caught_speeding(speed, is_birthday):
  if is_birthday:
    if speed <= 60+5:
      return 0
    elif speed >= 81+5:
      return 2
    else:
      return 1
  else:
    if speed <= 60:
      return 0
    elif speed >= 81:
      return 2
    else:
      return 1
