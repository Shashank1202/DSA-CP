'''
Problem Link:
https://leetcode.com/problems/implement-stack-using-queues/submissions/1264009586/
'''

from queue import Queue

class Stack:
    def __init__(self):
        self.q=Queue()


    def push(self, x):
        s=self.q.qsize()
        self.q.put(x)
        for i in range(s):
            self.q.put(self.q.get())


    def pop(self):
        n=self.q.get()
        return n

    def top(self):
        return self.q.queue[0]

    def size(self):
        return self.q.qsize()

if __name__=="__main__":
    s=Stack()
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(1)

    print("The top of stack",s.top())
    print("The size ",s.size())
    print("the deleted element:",s.pop())
    print("The top of stack:",s.top())
