class MyHashMap:

    def __init__(self):
        self.d = []

    def put(self, key: int, value: int) -> None:
        for i in self.d:
            if i[0] == key:
                i[1] = value
                return
        self.d.append([key,value])

    def get(self, key: int) -> int:
        for i in self.d:
            if i[0] == key:
                return i[1]
        return -1

    def remove(self, key: int) -> None:
        for i in self.d:
            if i[0] == key:
                self.d.remove(i)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
