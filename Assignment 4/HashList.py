class HashList:
    HashList = []
    length = None
    item_count = 0

    def __init__(self, length):
        self.HashList = [None] * length
        self.length = length

    def hashFunction(self, item):
        return item % self.length

    def put(self, item):
        index = self.hashFunction(item)
        first = index
        if self.item_count == self.length:
            raise IndexError
        while True:
            if self.HashList[index] == None:
                self.HashList[index] = item
                return
            index += 1
            if index > len(self.HashList):
                index = 0
            if index == first:
                return False
