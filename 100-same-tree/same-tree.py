class Solution:
    def isSameTree(self, p, q):
        
        # case 1:
        # agar dono nodes none hain (matlab dono trees me is position pe kuch nahi hai)
        # → structure match kar raha hai → is level pe same
        if p is None and q is None:
            return True
        
        # case 2:
        # agar ek node none hai aur dusra nahi
        # → ek tree me node hai aur dusre me nahi → structure mismatch
        # → poora tree same nahi ho sakta
        if p is None or q is None:
            return False
        
        # case 3:
        # dono nodes exist karte hain, lekin unki values alag hain
        # → value mismatch → trees same nahi
        if p.val != q.val:
            return False
        
        # case 4 (most important):
        # ab current node same hai (structure + value dono match)
        # ab check karna hai:
        # → left subtree same hai kya?
        # → right subtree same hai kya?
        #
        # dono true hone chahiye tabhi poora tree same hoga
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)