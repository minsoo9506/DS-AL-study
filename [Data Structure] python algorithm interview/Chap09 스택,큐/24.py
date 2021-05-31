# 스택을 이용한 큐 구현
class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        if no self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return self.input = [] and self.output = []