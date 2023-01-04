#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (39.96%)
# Likes:    15259
# Dislikes: 364
# Total Accepted:    1.4M
# Total Submissions: 3.4M
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in non-decreasing order, find the
# starting and ending position of a given target value.
# 
# If target is not found in the array, return [-1, -1].
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums is a non-decreasing array.
# -10^9 <= target <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [find_first_element_by_binary_search(nums,target),find_last_element_by_binary_search(nums,target)]

def find_first_element_by_binary_search(nums: List[int], target: int):
    left = 0
    right = len(nums) - 1
    if left > right:
        return -1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif mid == 0 or nums[mid - 1] != target:
            return mid
        else:
            right = mid - 1
    return -1

def find_last_element_by_binary_search(nums: List[int], target: int):
    left = 0
    right = len(nums) - 1
    if left > right:
        return -1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif mid == len(nums) - 1 or nums[mid + 1] != target:
            return mid
        else:
            left = mid + 1
    return -1
        
        
# @lc code=end

