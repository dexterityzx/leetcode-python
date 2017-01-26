'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

nums1 = [1,2,3,4]
nums2 = [2.1,3.1,4.1]

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    if len(nums1) == 0 or len(nums2) == 0:
    	return getMidian(nums1+nums2)
    # find nums1[0]'s location in nums2
    _idx = binSearch(nums2,nums1[0])
    mergedList = mergeList(nums1,nums2[_idx:])
    final_nums = nums2[:_idx] + mergedList
    print final_nums
    return getMidian(final_nums)

def mergeList(nums1,nums2):
	mergedList = list()
	n2_idx = 0
	for n1_idx in range(len(nums1)):
		while n2_idx<len(nums2) and nums2[n2_idx]<nums1[n1_idx]:
			mergedList.append(nums2[n2_idx])
			n2_idx += 1
		mergedList.append(nums1[n1_idx])
	while n2_idx<len(nums2) :
		mergedList.append(nums2[n2_idx])
		n2_idx += 1
	return mergedList   

def getMidian(nums):
    if len(nums) == 0:
        return 0

    midIdx = len(nums)/2
    if len(nums)%2 == 0:
        return float((nums[midIdx-1] + nums[midIdx]))/2
    else:
        return nums[midIdx]

def binSearch(nums,target):
	if len(nums) == 1:
		return 0
	mid = len(nums)/2
	if nums[mid] == target:
		return mid
	elif nums[mid] > target:
		return binSearch(nums[:mid],target)
	else:
		return mid+binSearch(nums[mid:],target)

# print binSearch([1,13,14,16],17)
print findMedianSortedArrays(nums1, nums2)