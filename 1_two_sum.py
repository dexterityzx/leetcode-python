'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    ### slow
    # for i in range(len(nums)):
    #     for j in range(i+1,len(nums)):
    #         if nums[i]+nums[j] == target:
    #             return [i,j]
    # return []
    ### faster
    _dict = {}
    for i in range(len(nums)):
    if nums[i] in _dict:
    return [_dict[nums[i]],i]
    else :
    _dict[target-nums[i]] = i
    return []