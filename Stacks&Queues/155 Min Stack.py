'''Problem link:
https://leetcode.com/problems/min-stack/description/
'''

class MinStack:

    def __init__(self):
        self.st= []
        self.mini= float('inf')

    def push(self, val: int) -> None:
        if not self.st:
            self.mini=val
            self.st.append((val, self.mini))
        else:
            self.mini= min(self.mini, val)
            self.st.append((val, self.mini))

    def pop(self) -> None:
        if not self.st:
            return
        self.st.pop()
        if self.st:
            self.mini=min(item[0] for item in self.st)
        else:
            self.mini=float('inf')

    def top(self) -> int:
        if not self.st:
            return None
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
