def array123(nums):
  a=[1,2,3]
  for i in range(len(nums)):
    temp=nums[i:i+3]
    if temp==a:
      return True
  return False
