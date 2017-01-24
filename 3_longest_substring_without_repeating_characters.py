'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
from collections import deque
string = "ohvhjdml"
def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        q = deque()
        max_len = len(q)
        for char in s:
        	print q
        	print max_len
        	if char not in q:
        		q.append(char)
        	else:
        		max_len = max(len(q),max_len)
        		idx = list(q).index(char)
        		for _ in range(idx+1):
        			q.popleft()
	        	q.append(char)
       	print q
        return max(len(q),max_len)

print lengthOfLongestSubstring(string)
