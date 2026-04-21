class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):  # PICHE SE CHALAO
            if digits[i] < 9:     # AGAR VALUE 8 SE CHOTI HAI TOH 
                digits[i] += 1   # USME ADD 1 KARDO
                return digits    # LOOP  KO END KARDO AND LIST RETURN KARDO
            digits[i] = 0    # US VALUE KO 0 SE INITILIZE KARDO
        
        return [1] + digits   # loop purA CHAL LIYE HO SO 1 [0 0 0 ] HO JAO