from Node import Node

class Linked_List():
    def __init__(self):
        self.head_node = None
    
    def __str__(self):
        output = ""
        current_node = self.head_node
        while (current_node != None):
            output += f"{current_node.get_value()}, "
            current_node = current_node.get_next()
        return f"[{output[:-2]}]"
    
    def add(self, item):
        new_Node = Node(item)
        if(self.head_node == None): 
            self.head_node = new_Node
            return
        currNode = self.head_node
        while (currNode.get_next() != None):
            currNode = currNode.get_next()
        currNode.set_next(new_Node)
            
    def remove(self, item):
        currNode = self.head_node
        prevNode = None
        while(currNode.get_value() != item):
            prevNode = currNode
            currNode = currNode.get_next()
        
        
    def search(self, item):
        current_node = self.head_node
        while(current_node.get_value != item):
            current_node = current_node.get_next()
        return current_node
    
    def isEmpty(self):
        pass
    def size(self):
        pass
    def append(self, item):
        pass
    def index(self, item):
        pass
    def insert(self, position, item):
        pass
    def pop(self, position = "Last####"):
        pass

if(__name__ == "__main__"):
    n = Linked_List()
    n.add(5)
    n.add("bean")
    print(n)
