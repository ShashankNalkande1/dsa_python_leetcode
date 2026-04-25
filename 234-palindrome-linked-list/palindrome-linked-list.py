class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []

        # store values
        while head:
            vals.append(head.val)
            head = head.next

        # check palindrome
        return vals == vals[::-1]
