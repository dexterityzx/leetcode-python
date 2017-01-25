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

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    l = len(nums1) if len(nums1)>len(nums2) else len(nums2)
    idx1 = 0
    idx2 = 0
    # for _ in range(l):
    # 	if nums1[idx1] >=

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

print binSearch([1,13,14,16],17)