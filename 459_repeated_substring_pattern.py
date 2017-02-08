'''
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1
Input abab

Output True

Explanation It's the substring ab twice.
Example 2
Input aba

Output False
Example 3
Input abcabcabcabc

Output True

Explanation It's the substring abc four times. (And the substring abcabc twice.)
'''
# brute force - slow
import math
def repeatedSubstringPattern(str):
    """
    :type str: str
    :rtype: bool
    """
    for i in xrange(1,len(str)):
        r = str[0:i]
        j = i
        while j<len(str):
            if r == str[j:j+len(r)]:
                j+=len(r)
            else:
                break
        if j==len(str):
            return True
        
    return False
# faster
def repeatedSubstringPattern2(str):
    """
    :type str: str
    :rtype: bool
    """
    l = int(math.sqrt(len(str)))
    n = len(str)
    # print l
    for i in xrange(1,l+1):
    	# print i
    	if n%i:
    		continue
    	else:
    		# print len(str)/i
    		L = n - i
    		if L!=0 and str[0:L] == str[n-L:]: 
    			# print i
    			return True
    		L = n -n/i
    		if L!=0 and str[0:L] == str[n-L:]: 
    			print i
    			return True
    return False

# print math.sqrt(10)
print repeatedSubstringPattern2('avbavb')
