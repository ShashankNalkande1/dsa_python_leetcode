class Solution(object):
    def reverseList(self, head):
        prev = None        # pehle koi previous node nahi hai, isliye none
        curr = head        # current node ko head se start karte hai

        while curr:        # jab tak current node exist karta hai
            next_temp = curr.next   # next node ko store karlo warna link toot jayega
            curr.next = prev        # current ka next reverse karke previous pe point kar do
            prev = curr             # prev ko aage badhao (current ban gaya prev)
            curr = next_temp        # current ko next node pe le jao

        return prev        # last me prev hi naya head banega reversed   list   ka