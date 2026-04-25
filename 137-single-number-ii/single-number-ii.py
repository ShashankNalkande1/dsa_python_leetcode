class Solution(object):  # 
    def singleNumber(self, nums): 
        dict1 = {}    # EMPTY HASHMAP DICT 

        for n in nums: #
            dict1[n] = dict1.get(n, 0) + 1

        for k, v in dict1.items():
            if v == 1:
                return k