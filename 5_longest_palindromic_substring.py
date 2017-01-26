'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
'''
"""
baabaad => aabaa

baa

"""
# get max length in recursive style => slow
def longestPalindromeLength(s):
	max_len = 0;
	if isPalindromic(s):
		return len(s)
	else:
		for i in range(1,len(s)):
			max_len = max(longestPalindrome(s[:i]),longestPalindrome(s[i:]),max_len)
		return max_len
# original answer
def longestPalindrome(s):
	ret_string = ''
	container = ''
	for i in range(len(s)):
		container += s[i]
		# print 'containter:' + container
		for j in range(len(container)):
			_s = container[j:len(container)]
			# print _s
			if isPalindromic(_s):
				if len(_s) >= len(ret_string):
					ret_string = _s
					break
	return ret_string
# this is much faster
def longestPalindrome2(s):
	ret_string = ''
	max_len = 0
	for i in range(len(s)):
		str1=findMaxPalindromic(s,i,i)
		str2=findMaxPalindromic(s,i,i+1)
		_str= str1 if len(str1)>len(str2) else str2
		ret_string = _str if len(_str)>len(ret_string) else ret_string
	return ret_string

def findMaxPalindromic(s,front,back):

	while front>=0 and back<len(s):
		if s[front] == s[back]:
			front -= 1
			back += 1
		else:
			break
	return s[front+1:back]

def isPalindromic(s):
	end = len(s) - 1
	for i in range(len(s)/2):
		if s[i] != s[end-i]:
			return False;
	return True

print longestPalindrome2("baabaad")