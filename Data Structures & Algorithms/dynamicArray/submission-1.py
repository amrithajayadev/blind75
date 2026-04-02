class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.size = 0


    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n 

    def pushback(self, n: int) -> None:
        if self.size == len(self.arr):
            self.resize()
        self.arr[self.size]=n
        self.size += 1

    def popback(self) -> int:
        element = self.arr[self.size-1]
        self.arr[self.size-1] = None
        self.size -= 1
        return element

    def resize(self) -> None:
        l = len(self.arr)
        new_arr = self.arr + [None]*l
        self.arr = new_arr 

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return len(self.arr)
