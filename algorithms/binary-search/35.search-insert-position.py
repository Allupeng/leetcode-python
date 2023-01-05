#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (42.34%)
# Likes:    11106
# Dislikes: 518
# Total Accepted:    1.9M
# Total Submissions: 4.5M
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array of distinct integers and a target value, return the
# index if the target is found. If not, return the index where it would be if
# it were inserted in order.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,3,5,6], target = 2
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,3,5,6], target = 7
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums contains distinct values sorted in ascending order.
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start
# 该问题可以抽象为 用binary_search找到第一个大于等于target的位置
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        if left > right:
            return -1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if mid == len(nums) - 1 or nums[mid + 1] > target:
                    return mid + 1
                else:
                    left = mid + 1
            elif nums[mid] > target:
                if mid == 0 or nums[mid - 1] < target:
                    return mid
                else:
                    right = mid - 1
        return -1
# @lc code=end

