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
        after_node = self.head_node
        self.head_node = new_Node
        new_Node.set_next(after_node)
            
    def remove(self, item):
        currNode = self.head_node
        prevNode = self.head_node
        if(self.head_node.get_value() == item):
            self.head_node = self.head_node.get_next()
            return
        while(currNode != None):
            if(currNode.get_value() == item):
                prevNode.set_next(currNode.get_next())
                return
            prevNode = currNode
            currNode = currNode.get_next()
        raise Exception("Item not in list!")
            
    def search(self, item):
        current_node = self.head_node
        while(current_node.get_value() != item):
            if(current_node.get_next() == None):
                return False
            current_node = current_node.get_next()
        return True
    
    def isEmpty(self):
        if(self.head_node == None):
            return True
        return False
    
    def size(self):
        current_node = self.head_node
        size = 0
        while(current_node != None):
            size += 1
            current_node = current_node.get_next()
        return size
    
    def append(self, item):
        new_Node = Node(item)
        if(self.head_node == None): 
            self.head_node = new_Node
            return
        currNode = self.head_node
        while (currNode.get_next() != None):
            currNode = currNode.get_next()
        currNode.set_next(new_Node)
        
    def index(self, item):
        if(not self.search(item)):
            raise Exception("Item not in list!")
        index = 0
        current_node = self.head_node
        while(current_node.get_value() != item):
            index += 1
            current_node = current_node.get_next()
        return index
        
    def insert(self, position, item):
        if(position > self.size() or position < 0):
            raise IndexError()
        newNode = Node(item)
        currNode = self.head_node
        index = 0
        prevNode = self.head_node
        while(position != index):
            prevNode = currNode
            currNode = currNode.get_next()
            index += 1
        if(position != 0):
            prevNode.set_next(newNode)
            newNode.set_next(currNode)
        if(position == 0):
            newNode.set_next(currNode)
            self.head_node = newNode
            
    def pop(self, position = None):
        if(position == None):
            position = self.size() - 1
        if(position > self.size() or position < 0):
            raise IndexError()
        currNode = self.head_node
        index = 0
        prevNode = self.head_node
        while(position != index):
            prevNode = currNode
            currNode = currNode.get_next()
            index += 1
        if(position != 0):
            prevNode.set_next(newNode)
            newNode.set_next(currNode)
        if(position == 0):
            newNode.set_next(currNode)
            self.head_node = newNode
        

if(__name__ == "__main__"):
    n = Linked_List()
    n.add(5)
    print(n)
    print(f"size: {n.size()}")
    n.add("bean")
    print(n)
    print(f"size: {n.size()}")
    n.remove("bean")
    print(n)
    print(f"size: {n.size()}")
    n.add("new")
    print(n)
    print(f"size: {n.size()}")
    n.remove(5)
    print(n)
    print(f"size: {n.size()}")
    print(f"index of new: {n.index('new')}")
    n.add("first")
    print(n)
    print(f"size: {n.size()}")
    print(f"index of new: {n.index('new')}")
    n.insert(0, "ins")
    print(n)
    print(f"size: {n.size()}")
