'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''
# slow but accepted
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # pick one a => find two sum = -a
    
    return_list = [];
    for i in range(len(nums)) : 
        _dict = {}
        target = -1*nums[i]
        for j in range(i+1, len(nums)) :
            if nums[j] in _dict :
                _list = sorted([nums[i],nums[_dict[nums[j]]],nums[j]])
                if _list not in return_list :
                    return_list.append(_list)
            else :
                _dict[target-nums[j]] = j
    return return_list;
# faster and accepted
def threeSum2(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # pick one a => find two sum = -a
    nums.sort()
    return_list = []
    for i in range(len(nums)) : 
        if i > 0 and nums[i] == nums[i-1]:
            print 'continue:' + str(i)
            continue
        _dict = {}
        target = -1*nums[i]
        for j in range(i+1, len(nums)) :
            if nums[j] in _dict :
                _list = [nums[i],nums[_dict[nums[j]]],nums[j]]
                if _list not in return_list:
                    return_list.append(_list)
            else :
                _dict[target-nums[j]] = j
    return return_list; 
# fastest
def threeSum3(nums):
    res = []
    nums.sort()
    for i in xrange(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1 
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    return res
# l = [-1,0,1,2,-1,-4]
l = [0,0,0,0]
print threeSum2(l)