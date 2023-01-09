#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (42.98%)
# Likes:    3174
# Dislikes: 270
# Total Accepted:    447.1K
# Total Submissions: 1M
# Testcase Example:  '16'
#
# Given a positive integer num, return true if num is a perfect square or false
# otherwise.
# 
# A perfect square is an integer that is the square of an integer. In other
# words, it is the product of some integer with itself.
# 
# You must not use any built-in library function, such as sqrt.
# 
# 
# Example 1:
# 
# 
# Input: num = 16
# Output: true
# Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
# 
# 
# Example 2:
# 
# 
# Input: num = 14
# Output: false
# Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an
# integer.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= num <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        while left <= right:
            mid = left + ((right - left) >> 1)
            if mid * mid == num:
                return True
            # 说明mid小了，往右区间找
            elif mid * mid < num:
                left = mid + 1
            # 说明mid大了，往左区间找
            elif mid * mid > num:
                right = mid - 1
        return False
        
# @lc code=end

