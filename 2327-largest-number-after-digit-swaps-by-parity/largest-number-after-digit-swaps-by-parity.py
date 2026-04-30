class Solution:
    def largestInteger(self, num: int) -> int:
        digits = list(str(num))
        
        odd = []
        even = []
        
        # step 1: separate
        for d in digits:
            if int(d) % 2 == 0:
                even.append(d)
            else:
                odd.append(d)
        
        # step 2: sort descending
        odd.sort(reverse=True)
        even.sort(reverse=True)
        
        i = 0  # pointer for odd
        j = 0  # pointer for even
        
        result = []
        
        # step 3: rebuild
        for d in digits:
            if int(d) % 2 == 0:
                result.append(even[j])
                j += 1
            else:
                result.append(odd[i])
                i += 1
        
        return int("".join(result))