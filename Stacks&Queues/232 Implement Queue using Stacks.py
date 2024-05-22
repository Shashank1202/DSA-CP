'''Problem link:
https://leetcode.com/problems/implement-queue-using-stacks/submissions/1264820757/
'''

class MyQueue:
    def __init__(self):
        # Initialize two stacks
        self.inputStack = []  # Stack for pushing new elements
        self.outputStack = []  # Stack for popping and peeking elements
        print(f"Initialized an empty queue")

    def push(self, value: int) -> None:
        # Push the value into the input stack
        self.inputStack.append(value)
        print(f"Pushed {value} to the queue. Input stack: {self.inputStack}, Output stack: {self.outputStack}")

    def pop(self) -> int:
        # If the output stack is empty, pop all elements from the input stack and push them into the output stack
        if not self.outputStack:
            while self.inputStack:
                self.outputStack.append(self.inputStack.pop())
        # Pop and return the top element from the output stack
        popped_value = self.outputStack.pop()
        print(f"Popped {popped_value} from the queue. Input stack: {self.inputStack}, Output stack: {self.outputStack}")
        return popped_value

    def peek(self) -> int:
        # If the output stack is empty, pop all elements from the input stack and push them into the output stack
        if not self.outputStack:
            while self.inputStack:
                self.outputStack.append(self.inputStack.pop())
        # Return the top element from the output stack
        peeked_value = self.outputStack[-1]
        print(f"Peeked {peeked_value} from the queue. Input stack: {self.inputStack}, Output stack: {self.outputStack}")
        return peeked_value

    def empty(self) -> bool:
        # Return whether both the input stack and the output stack are empty
        is_empty = not self.inputStack and not self.outputStack
        print(f"Checked if the queue is empty. Result: {is_empty}. Input stack: {self.inputStack}, Output stack: {self.outputStack}")
        return is_empty
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
