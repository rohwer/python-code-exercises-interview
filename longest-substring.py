# Longest Substring without Repeating Characters

# Given a string,
# find the length of the longest substring without repeating characters
#
# Example 1
# Input "abcabcbb"
# Output 3
# "abc" with length 3
# 
# Example 2
# Input "bbbbb"
# Output 1
# Explanation: answer is "b" with length 1
#
# Example 3
# Input "pwwkew"
# Output 3
# Explanation The answer is "wke"
# "pwke" is a subsequence not a substring
from itertools import combinations
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        largest = "1" 
        for size in range(2,len(s)):
            ls = s[start:size]
            
            # subsequence is not substring
            # so use a set to test unique characters
            if len(set(ls)) == (size - start):

                # Update if longer. Could use max and int
                # but I want to see the largest substring
                if len(ls) > len(largest):
                    largest = "".join(ls)
                    
            else:
                start += 1  # move window to find new substring
                
        return len(largest)

# 
# Solution, (easy to understand) per site, but clearly does not work
# https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/
def longest_substring(s):
    ls = []
    longest = 0
    for x in s:
        if x in ls:
            x = ls[ls.index(x)+1:] # this eventually returns the len(s)
        ls.append(x)
        longest = max(longest, len(ls))
    return longest
    
    
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(longest_substring("abcabcbb"))
    
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(longest_substring("bbbbb"))
    
    print(s.lengthOfLongestSubstring("pwwkew"))
    print(longest_substring("pwwkew"))    
    
