# Write an algorithm to determine if a number n is happy. 
# 
#  A happy number is a number defined by the following process: 
# 
#  
#  Starting with any positive integer, replace the number by the sum of the 
# squares of its digits. 
#  Repeat the process until the number equals 1 (where it will stay), or it 
# loops endlessly in a cycle which does not include 1. 
#  Those numbers for which this process ends in 1 are happy. 
#  
# 
#  Return true if n is a happy number, and false if not. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 19
# Output: true
# Explanation:
# 1² + 9² = 82
# 8² + 2² = 68
# 6² + 8² = 100
# 1² + 0² + 0² = 1
#  
# 
#  Example 2: 
# 
#  
# Input: n = 2
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 2³¹ - 1 
#  
# 
#  Related Topics Hash Table Math Two Pointers 👍 7965 👎 996


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isHappy(self, n: int) -> bool:
        if not n:
            return False
        sumSet = set()
        Sum = 0
        while Sum != 1:
            Sum = self.sumOfDigits(n)
            if Sum in sumSet:
                return False
            n = Sum
            sumSet.add(Sum)
        return True

    def sumOfDigits(self, n) -> int:
        Sum = 0
        while n != 0:
            Sum += (n % 10) * (n % 10)
            n //= 10
        return Sum
# leetcode submit region end(Prohibit modification and deletion)
