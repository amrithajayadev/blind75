class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hm = [Node(0, 0) for i in range(10000)]

    def put(self, key: int, value: int) -> None:
        bucket = key % 10000
        node = self.hm[bucket]
        while node.next:
            if node.next.key == key:
                node.next.val = value
                return
            node = node.next
        node.next = Node(key, value)
        

    def get(self, key: int) -> int:
        bucket = key % 10000
        node = self.hm[bucket]
        while node.next:
            if node.next.key == key:
                return node.next.val
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        bucket = key % 10000
        node = self.hm[bucket]
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)