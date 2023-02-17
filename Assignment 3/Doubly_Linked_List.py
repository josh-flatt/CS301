from Node import Node
from Linked_List import Linked_List

class Doubly_Linked_List(Linked_List):
    def __init__(self):
        self.headNode = None
        self.tailNode = None
        self.dllLength = 0
    
    def __str__(self):
        output = ""
        currNode = self.headNode
        while currNode != None:
            output += f"{currNode.get_value()}, "
            currNode = currNode.get_next()
        return f"[{output[:-2]}]"

    def add(self, item):
        newNode = Node(item)
        # if self.headNode == None:
        if self.dllLength == 0:
            self.headNode = newNode
            self.dllLength += 1
            return
        nextNode = self.headNode
        self.headNode = newNode
        newNode.set_next(nextNode)
        self.dllLength += 1

    def remove(self, item):
        currNode = self.headNode
        prevNode = self.headNode
        if self.headNode.get_value() == item:
            self.headNode = self.headNode.get_next()
            self.dllLength += -1
            return
        while currNode != None:
            if currNode.get_value() == item:
                prevNode.set_next(currNode.get_next())
                self.dllLength += -1
                return
            prevNode = currNode
            currNode = currNode.get_next()
        raise Exception("Item not in list!")

    def search(self, item):
        currNode = self.headNode
        while currNode.get_value() != item:
            if currNode.get_next() == None:
                return False
            currNode = currNode.get_next()
        return True

    def isEmpty(self):
        if self.headNode == None:
            return True
        return False

    def size(self):
        return self.dllLength
        # currNode = self.headNode
        # size = 0
        # while currNode != None:
        #     size += 1
        #     currNode = currNode.get_next()
        # return size

    def append(self, item):
        new_node = Node(item)
        if self.headNode == None:
            self.headNode = new_node
            self.dllLength += 1
            return
        currNode = self.headNode
        while currNode.get_next() != None:
            currNode = currNode.get_next()
        currNode.set_next(new_node)
        self.dllLength += 1

    def index(self, item):
        if not self.search(item):
            raise Exception("Item not in list!")
        index = 0
        currNode = self.headNode
        while currNode.get_value() != item:
            index += 1
            currNode = currNode.get_next()
        return index

    def insert(self, position, item):
        if position > self.size() or position < 0:
            raise IndexError()
        newNode = Node(item)
        currNode = self.headNode
        prevNode = self.headNode
        index = 0
        while position != index:
            prevNode = currNode
            currNode = currNode.get_next()
            index += 1
        if position != 0:
            prevNode.set_next(newNode)
            newNode.set_next(currNode)
        if position == 0:
            newNode.set_next(currNode)
            self.headNode = newNode
        self.dllLength += 1

    def pop(self, position=None):
        if position == None:
            position = self.size() - 1
        if position >= self.size() or position < 0:
            raise IndexError()
        currNode = self.headNode
        prevNode = self.headNode
        index = 0
        while position != index:
            prevNode = currNode
            currNode = currNode.get_next()
            index += 1
        if position != 0:
            prevNode.set_next(currNode.get_next())
            self.dllLength += -1
            return currNode.get_value()
        if position == 0:
            self.headNode = currNode.get_next()
            self.dllLength += -1
            return currNode.get_value()


if __name__ == "__main__":
    
    ########## Testing ###########
    
    dll = Doubly_Linked_List()
    dll.add(5)
    print(dll)
    print(f"size: {dll.size()}")
    dll.add("test")
    print(dll)
    print(f"size: {dll.size()}")
    dll.remove("test")
    print(dll)
    print(f"size: {dll.size()}")
    dll.add("new")
    print(dll)
    print(f"size: {dll.size()}")
    dll.remove(5)
    print(dll)
    print(f"size: {dll.size()}")
    print(f"index of new: {dll.index('new')}")
    dll.add("first")
    print(dll)
    print(f"size: {dll.size()}")
    print(f"index of new: {dll.index('new')}")
    dll.insert(0, "ins")
    print(dll)
    print(f"size: {dll.size()}")
    print(f'Popped "{dll.pop()}"')
    print(dll)
    print(f"size: {dll.size()}")
    print(f'Popped "{dll.pop(0)}"')
    print(dll)
    print(f"size: {dll.size()}")