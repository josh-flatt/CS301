class HashList:
    HashList = []
    length = None
    item_count = 0

    def __init__(self, length):
        self.HashList = [None] * length
        self.length = length

    def hashFunction(self, item):
        return item % self.length

    def rehash(self, index):
        first = index
        while True:
            if self.HashList[index] == None:
                return index
            index += 1
            if index >= len(self.HashList):
                index = 0
            if index == first:
                raise IndexError

    def put(self, item):
        index = self.hashFunction(item)
        first = index
        if self.item_count == self.length:
            raise IndexError
        while True:
            if self.HashList[index] == None:
                self.HashList[index] = item
                self.item_count += 1
                return
            index += 1
            if index >= len(self.HashList):
                index = 0
            if index == first:
                return False

    def contains(self, item):
        index = self.hashFunction(item)
        first = index
        if self.HashList[index] == item:
            return True
        if self.hashList[index] == None:
            return False
        while True:
            index += 1
            if index >= len(self.HashList):
                index = 0
            if self.hashList[index] == item:
                return True
            if self.HashList[index] == None:
                return False
            if index == first:
                return False

    def items(self):
        output = []
        for i in range(self.length - 1):
            if i != None:
                output.append(self.HashList[i])
            else:
                continue
        return output
