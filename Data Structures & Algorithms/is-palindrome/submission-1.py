class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        st = []
        for i in s:
            if i.isalnum():
                st.append(i)
        return st == st[::-1]