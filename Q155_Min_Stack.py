class MinStack:

    def __init__(self):
        self.items=[] #SC:O(N)
    #TC:(1)
    def push(self, value: int) -> None:
        if len(self.items)==0:
            self.items.append([value,value])
        else:
            mini = min(self.items[-1][1],value)
            self.items.append([value,mini])
    #TC:O(1)
    def pop(self) -> None:
        return self.items.pop()[0]
    #TC:O(1)
    def top(self) -> int:
        return self.items[-1][0]
    #TC:O(1)
    def getMin(self) -> int:
        return self.items[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()