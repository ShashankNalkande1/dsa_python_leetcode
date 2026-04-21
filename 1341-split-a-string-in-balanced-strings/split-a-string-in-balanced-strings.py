class Solution(object):
    def balancedStringSplit(self, s):
        r = 0
        l = 0
        res = 0

        for ch in s:
            if ch == 'R':
                r += 1
            else:
                l += 1

            if r == l:
                res += 1

        return res