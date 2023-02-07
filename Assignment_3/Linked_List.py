class Node():
    def __init__(self, item, previous_Node, next_Node):
        self.prevNode = previous_Node
        self.nextNode = next_Node
        self.item = item
    
    def get_previous_node(self):
        return self.prevNode

    def get_next_node(self):
        return self.nextNode
    
    def get_value(self):
        return self.item

class Linked_List():
    def __init__(self):
        self.frontNode = Node()
        self.endNode = Node()
    
