# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        dono pointer head per stand kar rahe hai  
        while/jab tak fast and fast.next hai 
        slow = slow next tak le jau
        and fast ko fast ko fast ke next ke next tak means do kadam
        
        """
        slow,fast = head,head  ## dono pointer head pe stand kar rahe hai 
        while fast and fast.next:  ## 
            slow = slow.next
            fast = fast.next.next
        return slow