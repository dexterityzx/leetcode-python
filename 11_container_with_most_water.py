'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
'''
height = [1,2,1]
# exceed time limit
def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    max_volumn = 0;
    for i in xrange(len(height)):
    	for j in xrange(i+1,len(height)):
    		min_h = height[i]
    		_len = j-i
    		if height[j] >= height[i]:
    			volumn = height[i]*_len
    		else:
    			min_h = min(min_h,height[j])
    			volumn = min_h*_len
    		max_volumn = max(volumn,max_volumn)
    return max_volumn
# Accepted
def maxArea2(height):
    """
    :type height: List[int]
    :rtype: int
    """
    max_volumn = 0;
    i = 0
    j = len(height)-1
    while j>i :
    	_height = min(height[i],height[j])
    	max_volumn = max(_height*(j-i),max_volumn)
    	if height[i] > height[j] :
    		j -= 1
    	else:
    		i += 1
    return max_volumn


print maxArea2(height)