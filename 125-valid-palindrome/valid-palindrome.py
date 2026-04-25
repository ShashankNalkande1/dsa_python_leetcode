class Solution(object):
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:

            # left ko aage badhao jab tak valid char na mile
            while left < right and not s[left].isalnum():
                left += 1

            # right ko peeche lao jab tak valid char na mile
            while left < right and not s[right].isalnum():
                right -= 1

            # compare karo (case ignore)
            if s[left].lower() != s[right].lower():
                return False

            # dono pointers move karo
            left += 1
            right -= 1

        return True