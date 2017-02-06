'''
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
'''

dp =list();
# Top Down - slow   
def combinationSum4TD(nums,target):
    if self.dp[target] != -1:
        return self.dp[target]
    total = 0
    for i in xrange(len(nums)):
        diff = target - nums[i]
        if diff>=0 :
            total += self.combinationSum4TD(nums,diff)
    self.dp[target] = total
    return total
# button up - fast
def combinationSum4BU(nums,target):
    comb=[1]+[0]*target
    for i in xrange(1,len(comb)):
        for n in nums:
            if i-n >=0:
                comb[i] += comb[i - n]
    return comb[-1]

nums = [1, 2, 3]
target = 4
# print sorted(nums)
print combinationSum4BU(nums,target)