# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/
#
# Approach: two pointers, in place.
# i reads through the list. write marks the next free spot at the front.
# Every non-zero number is copied to position write, then write moves forward.
# After the loop, all non-zero numbers are packed at the front in their original order,
# so every position from write to the end is overwritten with 0.
#
# Time: O(n), two passes over the list.
# Space: O(1), no second list, only one counter.

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        write = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[write] = nums[i]
                write += 1

        for i in range(write, len(nums)):
            nums[i] = 0
