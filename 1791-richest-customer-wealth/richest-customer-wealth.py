class Solution(object):
    def maximumWealth(self, accounts):
        wealth_list = []

       
        for customer in accounts:
            total = 0
            for money in customer:
                total += money
            wealth_list.append(total)

        
        return max(wealth_list)