def centered_average(nums):
  a = max(nums)
  b = min(nums)
  c = len(nums) - 2
  d = sum(nums)
  
  return (d-(a+b))//c
