class Bucket:
    def __init__(self):
        self.bucket = []
    def update(self, key, value):
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                self.bucket[i] = (key, value)
                return
        self.bucket.append((key, value))
    
    def get(self, key):
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                return kv[1]
        return -1
    
    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                self.bucket.pop(i)
                break

class MyHashMap:

    def __init__(self):
        self.mod = 2069
        self.values = [Bucket() for _ in range(self.mod)]

    def put(self, key: int, value: int) -> None:
        index = key % self.mod
        self.values[index].update(key, value)

    def get(self, key: int) -> int:
        index = key % self.mod
        return self.values[index].get(key)

    def remove(self, key: int) -> None:
        index = key % self.mod
        self.values[index].remove(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
