# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/
#
# Approach: two pointers.
# Walk through t one character at a time. pos counts how many characters of s have been matched so far.
# When t[i] matches s[pos], move pos forward.
# The pos < len(s) check goes first so we never read past the end of s.
# If pos reaches len(s), every character of s was found in order, so s is a subsequence of t.
#
# Time: O(len(t)), one pass through t.
# Space: O(1), only one counter.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pos = 0
        for i in range(len(t)):
            if pos < len(s) and s[pos] == t[i]:
                pos += 1

        return pos == len(s)
