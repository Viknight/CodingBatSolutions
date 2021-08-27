def make_ends(nums):
  if len(nums) >= 1:
    return nums[:1] + nums[len(nums)-1:]
  else:
    return nums
