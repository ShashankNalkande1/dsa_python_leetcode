class Solution(object):
    def findTheDifference(self, s, t):
        xorans = 0

        for ch in s:
            xorans ^= ord(ch)

        for ch in t:
            xorans ^= ord(ch)

        return chr(xorans)