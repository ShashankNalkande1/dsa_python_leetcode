class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        x = 0
        result = []
        for i in range(len(nums)):
            x = x + nums[i]
            result.append(x)
        return result
            
            
            
           
        