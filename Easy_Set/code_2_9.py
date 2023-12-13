# Given an integer x, return true if x is a palindrome, and false otherwise.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        i = 0;
        j = len(str_x) - 1
        while(i < j):
            if(str_x[i] == str_x[j]):
                i = i + 1
                j = j - 1
            else:
                return False
        return True
    
