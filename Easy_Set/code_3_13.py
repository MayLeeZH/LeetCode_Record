# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.


class Solution:
    def romanToInt(self, s: str) -> int:
        skip_flag = False
        sum = 0
        length = len(s)
        for i,ch in enumerate(s):
            if(skip_flag == True):
                skip_flag = False
                continue

            if(ch == 'M'):
                sum += 1000
            elif( ch == 'D' ):
                sum += 500
            elif( ch == 'C' ):
                if( i + 1 < length):
                    if(s[i+1] == 'D'):
                        skip_flag = True
                        sum += 400
                    elif(s[i+1] == 'M'):
                        sum += 900
                        skip_flag = True
                if(skip_flag == False):
                    sum += 100
            elif( ch == 'L' ):
                sum += 50
            elif( ch == 'X' ):
                if( i + 1 < length):
                    if(s[i+1] == 'L'):
                        skip_flag = True
                        sum += 40
                    elif(s[i+1] == 'C'):
                        sum += 90
                        skip_flag = True
                if(skip_flag == False):
                    sum += 10
            elif( ch == 'V' ):
                sum += 5
            elif( ch == 'I' ):
                if( i + 1 < length):
                    if(s[i+1] == 'V'):
                        skip_flag = True
                        sum += 4
                    elif(s[i+1] == 'X'):
                        sum += 9
                        skip_flag = True
                if(skip_flag == False):
                    sum += 1
        return sum

sol = Solution()
result = sol.romanToInt("MCMXCIV")
print(result)
