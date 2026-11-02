# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/
#
# Approach: running total.
# Keep a total that grows as we move through nums. At each index, add nums[i] to the total
# and append the total to the result list.
#
# Time: O(n), one pass through nums, constant work at each step.
# Space: O(n) for the result list, which has the same size as nums.
#        Only O(1) extra space apart from the output (just total and i).

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            result.append(total)
        return result
