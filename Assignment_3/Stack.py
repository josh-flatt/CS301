class Stack:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        return str(self.items)
    
    def push(self, item) -> None:
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[:-1]
    
    def isEmpty(self) -> bool:
        return self.items == []

    def size(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.items = []
        
    def __str__(self):
        return str(self.items)
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

class Deque():
    def __init__(self):
        self.items = []
        
    def __str__(self):
        return str(self.items)
    
    def addFront(self, item):
        self.items.insert(0, item)
    
    def addRear(self, item):
        self.items.append(item)
    
    def removeFront(self):
        return self.items.pop(0)
    
    def removeRear(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)