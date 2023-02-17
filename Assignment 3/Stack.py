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