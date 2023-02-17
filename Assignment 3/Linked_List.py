from Node import Node

class Linked_List:
    def __init__(self):
        self.headNode = None

    def __str__(self):
        output = ""
        currNode = self.headNode
        while currNode != None:
            output += f"{currNode.get_value()}, "
            currNode = currNode.get_next()
        return f"[{output[:-2]}]"

    def add(self, item):
        newNode = Node(item)
        if self.headNode == None:
            self.headNode = newNode
            return
        nextNode = self.headNode
        self.headNode = newNode
        newNode.set_next(nextNode)

    def remove(self, item):
        currNode = self.headNode
        prevNode = self.headNode
        if self.headNode.get_value() == item:
            self.headNode = self.headNode.get_next()
            return
        while currNode != None:
            if currNode.get_value() == item:
                prevNode.set_next(currNode.get_next())
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
        currNode = self.headNode
        size = 0
        while currNode != None:
            size += 1
            currNode = currNode.get_next()
        return size

    def append(self, item):
        new_node = Node(item)
        if self.headNode == None:
            self.headNode = new_node
            return
        currNode = self.headNode
        while currNode.get_next() != None:
            currNode = currNode.get_next()
        currNode.set_next(new_node)

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
            return currNode.get_value()
        if position == 0:
            self.headNode = currNode.get_next()
            return currNode.get_value()


# if __name__ == "__main__":
    
    ########### Testing ###########
    
    # linked_list = Linked_List()
    # linked_list.add(5)
    # print(linked_list)
    # print(f"size: {linked_list.size()}")
    # linked_list.add("test")
    # print(linked_list)
    # print(f"size: {linked_list.size()}")
    # linked_list.remove("test")
    # print(linked_list)
    # print(f"size: {linked_list.size()}")
    # linked_list.add("new")
    # print(linked_list)
    # print(f"size: {linked_list.size()}")
    # linked_list.remove(5)
    # print(linked_list)
    # print(f"size: {linked_list.size()}")
    # print(f"index of new: {linked_list.index('new')}")
    # linked_list.add("first")
    # print(linked_list)
    # print(f"size: {linked_list.size()}")
    # print(f"index of new: {linked_list.index('new')}")
    # linked_list.insert(0, "ins")
    # print(linked_list)
    # print(f"size: {linked_list.size()}")
    # print(f'Popped "{linked_list.pop()}"')
    # print(linked_list)
    # print(f"size: {linked_list.size()}")
    # print(f'Popped "{linked_list.pop(0)}"')
    # print(linked_list)
    # print(f"size: {linked_list.size()}")
