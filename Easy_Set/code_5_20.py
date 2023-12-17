# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#  "{[]}()" true 
#  "({)}"" false 

# Misunderstand the meaning of the question
# class Solution:
#     def isValid(self, s: str) -> bool:
#         length = len(s)
#         found_flag = False
#         # if(length%2 == 1):
#         #     return False
#         found_list = [0] * length
#         for i , par_1 in enumerate(s):
#             if(found_list[i] == 0):
#                 found_list[i] = 1
#             else:
#                 continue
#             for j,par_2 in enumerate(s[i+1:]):
#                 if(found_list[j+i+1] == 1):
#                     continue
#                 if(par_1 == '('and par_2 ==')'):
#                     found_flag = True
#                     found_list[j+i+1] = 1
#                     break
#                 elif(par_1 == '{'and par_2 =='}'):
#                     found_flag = True
#                     found_list[j+i+1] = 1
#                     break
#                 elif(par_1 == '['and par_2 ==']'):
#                     found_flag = True
#                     found_list[j+i+1] = 1
#                     break
#             if(found_flag == True):
#                 found_flag = False
#             else:
#                 return False
#         return True



# Using Stack and Hash table
class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)
        if(length%2 == 1):
            return False
        stack = list()
        # Use hash table to quick match
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        for ch in s:
            if ch in pairs.keys():
                if  len(stack) != 0 and pairs[ch] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
            else:
                # Push into stack
                stack.append(ch)

        if len(stack) == 0:
            return True
        else:
            return False




# Test 
s = "){"
sol = Solution()
result = sol.isValid(s)
print(result)