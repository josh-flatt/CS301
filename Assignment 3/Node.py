class Node():
    def __init__(self, item):
        self.item = item
        self.nextNode = None
        self.prevNode = None

    def get_value(self):
        return self.item
    
    def get_next(self):
        return self.nextNode
    
    def set_next(self, newNode):
        self.nextNode = newNode
        
    def get_prev(self):
        return self.prevNode
    
    def set_prev(self, newNode):
        self.prevNode = newNode
