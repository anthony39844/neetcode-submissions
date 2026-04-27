class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        we sort these two lists by the position, keeping correlation between the speed and pos
        we sort in reverse order since a fleet can only form with cars from behind catching up
        if the time at the top of the stack is less than the current time, we know a fleet wont form
        since that car(s) will finish before this one does
        if the time is greater than or equal, we know that the current car will catch up
        resulting in a fleet 
        '''
        p, s = zip(*sorted(zip(position, speed), reverse=True))
        p, s = list(p), list(s)
        st = []
        for i, x in enumerate(p):
            t = ((target - x) / s[i])
            if st and st[-1] >= t:
                continue
            st.append(t)

        return len(st)


