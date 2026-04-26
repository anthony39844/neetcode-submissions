class MinStack:
    '''
    we keep a second stack for the min vals
    at each index, we have the min val for the current length of the list
    because we keep appending the min if the incoming val is greater than
    our current min val
    so as we pop off the from the main stack, we also pop from the min stack
    so when we pop the min from the main stack itll reflect on the min stack
    '''
    def __init__(self):
        self.s = []
        self.m = []

    def push(self, val: int) -> None:
        self.s.append(val)
        # if val is greater than the most recent min, append the current min
        if self.m and val > self.m[-1]:
            self.m.append(self.m[-1])
        else:
        # append smaller val
            self.m.append(val)

    def pop(self) -> None:
        self.s.pop()
        self.m.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.m[-1]