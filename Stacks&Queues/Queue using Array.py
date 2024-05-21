'''
Problem Link::
https://www.geeksforgeeks.org/problems/implement-queue-using-array/1
'''

class Solution:
    def __init__(self):
        self.start=-1
        self.end=-1
        self.currSize=0
        self.maxSize=5
        self.arr=[0]*self.maxSize

    def push(self, x:int)->None:
        if self.currSize==self.maxSize:
            print("The queue is full")
            exit(1)
        if self.end==-1:
            self.start=0
            self.end=0
        else:
            self.end=(self.end+1)%self.maxSize
        self.arr[self.end]=x
        self.currSize+=1

    def pop(self)->int:
        if self.start==-1:
            print("Queue is empty")
        popped=self.arr[self.start]
        if self.currSize==-1:
            self.start=-1
            self.end=-1
        else:
            self.start=(self.start+1)%self.maxSize
        self.currSize-=1
        return popped

    def Top(self)->int:
        if self.start==-1:
            print("Queue is empty")
            exit(1)
        return self.arr[self.start]

    def size(self)->int:
        return self.currSize


if __name__=="__main__":
    q=Solution()
    q.push(1)
    q.push(2)
    q.push(4)
    print("the peek of queue before deleting ",q.Top())
    print("The size of queue before deletion",q.size())
    print("The deleted elemnt is",q.pop())


