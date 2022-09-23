from cmath import inf


class minHeap():
    def __init__(self, size):
        self.filledSize = 0
        self.array = [inf] * size
        self.size = size

    def parentIndex(self, index):
        return (index - 1) // 2
    
    def leftChildIndex(self, index):
        return (2 * index) + 1

    def rightChildIndex(self, index):
        return (2 * index) + 2
    
    def hasParent(self, index):
        return self.parentIndex(index) >= 0

    def hasleftChild(self, index):
        return self.leftChildIndex(index) < self.size

    def hasRightChild(self, index):
        return self.rightChildIndex(index) < self.size

    def parent(self, index):
        return self.array[ self.parentIndex(index) ]
    
    def leftChild(self, index):
        return self.array[ self.leftChildIndex(index) ]
    
    def rightChild(self, index):
        return self.array[ self.rightChildIndex(index) ]

    def full(self):
        return self.filledSize == self.size

    def swapIndices(self, index1, index2):
        self.array[index2], self.array[index1] = self.array[index1], self.array[index2]
    
    def heapUp(self, index):
        if(self.hasParent(index) and self.parent(index) > self.array[index]):
            self.swapIndices(self.parentIndex(index), index)
            self.heapUp(self.parentIndex(index))
    
    def heapDown(self, index):
        smallest = index
        if(self.hasleftChild(index) and self.array[smallest] > self.leftChild(index)):
            smallest = self.leftChildIndex(index)
        if(self.hasRightChild(index) and self.array[smallest] > self.rightChild(index)):
            smallest = self.rightChildIndex(index)
        if(smallest != index):
            self.swapIndices(index, smallest)
            self.heapDown(smallest)

    def insert(self, data):
        if(self.full()):
            raise("Heap is full")
        
        self.array[self.filledSize] = data
        self.filledSize += 1
        self.heapUp(self.filledSize - 1)
    
    def remove(self):
        if(self.filledSize == 0):
            raise("Heap is empty")
        
        data = self.array[0]
        self.array[0] = self.array[self.filledSize - 1]
        self.array[self.filledSize - 1] = inf
        self.filledSize -= 1
        self.heapDown(0)
        return data
    
    def print(self):
        print(self.array)
    
if __name__ == '__main__':
    heap = minHeap(20)
    lst = [10, 20, 5, 8, 0, 15, 30]
    for num in lst:
        heap.insert(num)

    print(heap.remove()) #0
    print(heap.remove()) #5
    print(heap.remove()) #8
    print(heap.remove()) #10
    print(heap.remove()) #15
    print(heap.remove()) #20
    print(heap.remove()) #30
    # print(heap.remove()) #exception

    