class Solution:
    def isSymmetric(self, root):
        # yeh helper function do nodes ko compare karta hai ki kya yeh mirror position pe same hain
        def mirror(a, b):
            
            # case 1: dono nodes none hain
            # matlab dono side pe koi node hi nahi hai → structure match kar raha hai
            if a is None and b is None:
                return True
            
            # case 2: ek node none hai aur dusra nahi
            # matlab ek side pe node hai aur dusri side pe missing hai → structure mismatch
            if a is None or b is None:
                return False
            
            # case 3: dono nodes exist karte hain lekin values alag hain
            # matlab same position pe different value → symmetric nahi ho sakta
            if a.val != b.val:
                return False
            
            # case 4: ab current nodes same hain (structure + value match)
            # ab asli kaam yahan start hota hai:
            # hume mirror check karna hai, normal left-left nahi
            
            # important:
            # a.left ko b.right se compare karenge (outer mirror)
            # a.right ko b.left se compare karenge (inner mirror)
            
            # dono recursive calls true honi chahiye tabhi yeh subtree symmetric mana jayega
            return mirror(a.left, b.right) and mirror(a.right, b.left)
        
        # yahan hum tree ko khud se compare kar rahe hain
        # root ka left subtree aur root ka right subtree mirror hona chahiye
        # isliye mirror(root, root) call karte hain
        return mirror(root, root)