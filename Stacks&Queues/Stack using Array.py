'''
Problem Link:
https://www.geeksforgeeks.org/problems/implement-stack-using-array/1
'''
class Stack:
    def __init__(self):
        self.top =-1
        self.size= 1000
        self.arr=[0]*self.size

    def push(self, x: int)->None:
        self.top +=1
        self.arr[self.top]=x

    def pop(self)->int:
        x=self.arr[self.top]
        self.top -=1
        return x

    def Top(self)->int:
        return self.arr[self.top]

    def Size(self)->int:
        return self.top +1


if __name__=="__main__":
    s=Stack()
    s.push(2)
    s.push(4)
    s.push(7)
    print("The top element is ",s.Top())
    print("the size is ",s.Size())
    print("The last element pop is ",s.pop())
    print("The top element is ",s.Top())
