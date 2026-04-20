class Solution(object):
    def removeElement(self, nums, val):
        
        i = 0  # yeh write pointer hai, yahan next valid value store hogi

        for j in range(len(nums)):   # yeh loop har element ko check karega (read pointer)

            if nums[j] != val:       # agar current value remove wali value ke equal nahi ha

                nums[i] = nums[j]    # toh usko aage shift kar do

                i += 1               # next position ke liye pointer badhao

        return i                     # total valid elements ka count return karo