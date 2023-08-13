class ListNode:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size) -> None:
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        idx = self._hash(key)
        if self.table[idx] is None:
            self.table[idx] = ListNode(key, value)

        else:
            current = self.table[idx]
            while current.next:
                current = current.next

            current.next = ListNode(key, value)

    def get(self, key):
        idx = self._hash(key)
        current = self.table[idx]
        while current:
            if current.key == key:
                return f"{current.key} is "+ current.value
            current = current.next
        return f"{key} Not Found!"

    def remove(self, key):
        idx = self._hash(key)
        current = self.table[idx]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[idx] = current.next
            prev = current
            current = current.next

if __name__ == "__main__":
    hashmap = HashTable(10)
    hashmap.put("S400", "SAM")
    hashmap.put("Brahmos", "Anti-Ship Missile")
    hashmap.put("Astra", "BVR")
    print(hashmap.get("Brahmos"))
    hashmap.remove("S400")
    print(hashmap.get("S400"))