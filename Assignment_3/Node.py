class Node():
    def __init__(self, item):
        self.item = item
        self.nextNode = None

    def get_next(self):
        return self.nextNode
    
    def set_next(self, new_node):
        self.nextNode = new_node
        
    def get_value(self):
        return self.item
