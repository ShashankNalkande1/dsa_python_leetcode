class Solution(object):
    def toLowerCase(self, s):
        res = []  # result store

        for c in s:  # har char pe loop
            if 'A' <= c <= 'Z':  # uppercase check
                res.append(chr(ord(c) + 32))  # lower me convert
            else:
                res.append(c)  # same rakh

        return "".join(res)  # list → string