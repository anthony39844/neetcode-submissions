class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        st = set(s[0])
        out = 1
        l, r = 0, 1
        while r < len(s):
            if s[r] in st:
                out = max(out, r - l)
                while s[r] in st:
                    st.remove(s[l])
                    l += 1
                st.add(s[r])
            st.add(s[r])
            r += 1
        
        return max(out, r - l)


