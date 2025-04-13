class Stack: # stack implementaion using list
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity
    def __str__(self):
        return ', '.join(str(ele) for ele in self.stack)
    def push(self, data):
        if self.isFull():
            # print(f'stack full')
            pass
        else:
            self.stack.append(data)
    def pop(self):
        if self.isEmpty():
            # print(f'stack empty')
            return None
        else:
            return self.stack.pop()
    def isEmpty(self):
        return len(self.stack) == 0
    def isFull(self):
        return len(self.stack) >= self.capacity
    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]

class Queue: # queue implementaion using list
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity
    def __str__(self):
        return ', '.join(str(ele) for ele in self.queue)
    def enque(self, data):
        if self.isFull():
            # print(f'queue full')
            pass
        else:
            self.queue.append(data)
    def deque(self):
        if self.isEmpty():
            # print(f'queue empty')
            return None
        else:
            return self.queue.pop(0)
    def isEmpty(self):
        return len(self.queue) == 0
    def isFull(self):
        return len(self.queue) >= self.capacity
    def peek(self):
        if self.isEmpty():
            return None
        return self.queue[0]