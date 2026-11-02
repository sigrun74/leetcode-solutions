# 724. Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/
#
# Approach: prefix sum.
# Compute the total of the list once. Keep left as the running sum of everything before index i.
# The right sum is total - left - nums[i]: everything, minus the left part, minus the pivot itself.
# Return the first i where left equals right, otherwise -1.
# After checking i, add nums[i] to left so it is ready for the next index.
#
# Time: O(n), one pass to get the total and one pass over the list.
# Space: O(1), only a few variables.
#
# First attempt: recompute sum(nums[:i]) and sum(nums[i+1:]) for every i, O(n^2). It passed, but was very slow.

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left = 0
        for i in range(len(nums)):
            right = total - left - nums[i]
            if left == right:
                return i
            left += nums[i]
        return -1
