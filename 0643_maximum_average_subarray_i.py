"""
643. Maximum Average Subarray I

Pattern: fixed-size sliding window.
Approach: sum the first k numbers once. Then slide the window one step at a time:
add the number that enters (nums[i]) and subtract the number that leaves
(nums[i - k]), and keep the biggest sum seen. Divide by k once at the end.

Time: O(n), one pass.
Space: O(1) for the window idea (my nums[:k] slice makes it O(k) in practice).
"""


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        window = sum(nums[:k])
        maxavg = window

        for i in range(k, len(nums)):
            window += nums[i] - nums[i - k]
            if window > maxavg:
                maxavg = window

        return maxavg / k
