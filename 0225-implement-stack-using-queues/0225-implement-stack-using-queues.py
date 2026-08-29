from queue import Queue
class MyStack:

    def __init__(self):
        self.obj= Queue()

    def push(self, x: int) -> None:
        self.obj.put(x)
        for _ in range(self.obj.qsize()-1):
            self.obj.put(self.obj.get())

    def pop(self) -> int:
        return self.obj.get()
        
    def top(self) -> int:
        return self.obj.queue[0]

    def empty(self) -> bool:
        return self.obj.empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()