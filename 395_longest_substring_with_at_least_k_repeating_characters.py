'''
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
'''

def longestSubstring(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    # rlt_sum = 0
    # for i in range(0,len(s)):
    #     _dict = {}
    #     for j in range(0,i+1):
    #         if s[j] in _dict:
    #             _dict[s[j]] += 1
    #         else:
    #             _dict[s[j]] = 1
    #     # print _dict
    #     _sum = 0
    #     for l in _dict.itervalues():
    #         # print l
    #         if l >= k:
    #             _sum += l
    #         else:
    #             _sum = 0
    #             break
    #     # print _sum
    #     if _sum != 0:
    #         rlt_sum = max(_sum,rlt_sum)
    # return rlt_sum
    ################
    # if len(s) < k:
    #     return 0
    # _min_num_char = min(set(s), key=s.count)
    # if s.count(_min_num_char) >= k:
    #     return len(s)
    # return max(longestSubstring(sub_s,k) for sub_s in s.split(_min_num_char))
    print set(s)
    for c in set(s):
        if s.count(c) < k:
            # print c
            return max(longestSubstring(sub_s, k) for sub_s in s.split(c))
    return len(s)

s = "bbaaacbd"
print longestSubstring(s,3)
# s_test = "c"
# print s_test.split('c')
# print set(s_test)
# print min(set(s), key = s.count)

