class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class MyHashSet:

    def __init__(self):
        self.arr = [-1] * 10000
    
    def add(self, key: int) -> None:
        bucket = key % 10000
        if self.arr[bucket] == -1:
            head = Node(0)
            head.next = Node(key)
            self.arr[bucket] = head
        else:
            node = self.arr[bucket]
            while node.next:
                if node.next.val == key:
                    return
                node = node.next
            node.next = Node(key)
            

    def remove(self, key: int) -> None:
        bucket = key % 10000
        node = self.arr[bucket]
        if node == -1:
            return
        while node.next:
            if node.next.val == key:
                break
            node = node.next
        node.next = node.next.next if node.next else None
        

    def contains(self, key: int) -> bool:
        bucket = key %10000
        node = self.arr[bucket]
        if node == -1:
            return False
        else:
            node = node.next

        while node:
            if node.val == key:
                return True
            node = node.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)