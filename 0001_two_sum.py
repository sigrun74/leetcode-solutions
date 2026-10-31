# 1. Two Sum
# https://leetcode.com/problems/two-sum/
#
# Approach: one pass with a dictionary.
# For each number, work out the partner we need (target - number).
# If the partner is already in the dictionary, return its stored index and the current index.
# Otherwise store the current number with its index, so later numbers can find it.
#
# Time: O(n), each number is looked at once and a dictionary lookup is O(1).
# Space: O(n), the dictionary can hold up to n numbers.
#
# Brute force alternative: check every pair, O(n^2) time and O(1) extra space.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in seen:
                return [seen[need], i]
            seen[nums[i]] = i
