# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        length = len(strs)
        longest_common_prefix = strs[0]
        New_LCP = ''
        for str_ in strs:
            if(str_ == ""):
                return ""
            if (str_ == longest_common_prefix):
                continue
            for i in range(min(len(str_),len(longest_common_prefix))):
                if(str_[i] == longest_common_prefix[i]):
                    New_LCP += str_[i]
                else:
                    longest_common_prefix = New_LCP
                    New_LCP = ''
                    break
                if(i+1 == min(len(str_),len(longest_common_prefix))):
                    longest_common_prefix = New_LCP
                    New_LCP = ''
                    break
          
        return longest_common_prefix

# Test
sol = Solution()
strs = ["abab","aba",""]
result = sol.longestCommonPrefix(strs)
print(result)
