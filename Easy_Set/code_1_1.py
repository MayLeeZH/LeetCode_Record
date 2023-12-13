# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.



from typing import List

# Brute Force Approach
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         length = len(nums)
#         for i in range(len(nums)):
#             for j in range(i+1,length):
#                 if(nums[i] + nums[j] == target):
#                     return[i,j]

# Hash table 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = dict()
        for i,num in enumerate(nums):
            if(target - num in hash_table):
                return[i,hash_table[target - num]]
            hash_table[num] = i
        return []
            


# Test
# sol = Solution()
# result = sol.twoSum([2,7,11,15],9)
# print(result)