class Solution(object):
    def singleNumber(self, nums):
        res = 0  # start from 0

        for n in nums:
            res = res ^ n  # xor: same number cancels (a^a=0), 0^a=a

        return res  # only single nm left