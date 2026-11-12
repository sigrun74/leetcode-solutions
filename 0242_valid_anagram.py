"""
242. Valid Anagram

Pattern: count the letters with a dictionary.
Approach: if the lengths differ, return False. Then count each letter in s
(add 1), count each letter in t (subtract 1), and check that every count is 0.

Time: O(n), each word is read once.
Space: O(1), the dictionary holds at most 26 lowercase letters.
(If the input could be Unicode, space would be O(k) for k distinct characters.)
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        counts = {}

        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1

        for ch in t:
            counts[ch] = counts.get(ch, 0) - 1

        for v in counts.values():
            if v != 0:
                return False

        return True
