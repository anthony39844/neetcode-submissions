class Solution:
    def checkValidString(self, s: str) -> bool:
        o = []
        star = []

        for i in range(len(s)):
            if s[i] == "(":
                o.append(i)
            elif s[i] == "*":
                star.append(i)
            else:
                if o:
                    o.pop()
                elif star:
                    star.pop()
                else:
                    return False
        print(o, star)
        while o:
            if not star:
                return False
            x = o.pop()
            y = star.pop()
            if x > y:
                return False
        
        return True