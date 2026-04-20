class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        '''
        we loop through s2 
        if we run across a character that is in s1, then we call a backtrack func
        that will take in our current index and s1 - char
        we will continue recursively calling this func until either s1 is empty string
        or we run into a char that is not next in s2. 
        if s1 becomes empty string, then we return True
        else if we run into something that is not next in s2, we return False and then continue 
        '''


        def func(s, ind):
            if s == "":
                return True
            if s2[ind] not in s:
                return False
            else:
                return func(s.replace(s2[ind], "", 1), ind + 1)

        for i, char in enumerate(s2):
            if len(s2) - i < len(s1):
                return False
            if char in s1:
                if func(s1.replace(char, "", 1), i + 1):
                    return True
        
        return False
