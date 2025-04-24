class DynamicArray:
    def __init__(self):
        self.__capacity = 10
        self.__size = 0
        self.__arr = [None] * self.__capacity

    def push_back(self, value):
        if self.__size == self.__capacity:
            self.__resize(self.__capacity * 2)
        self.__arr[self.__size] = value
        self.__size += 1

    def pop_back(self):
        if self.__size == 0:
            raise IndexError("pop from empty array")
        self.__size -= 1
        self.__arr[self.__size] = None

    def size(self):
        return self.__size

    def capacity(self):
        return self.__capacity

    def __resize(self, new_size):
        new_arr = [None] * new_size
        for i in range(self.__size):
            new_arr[i] = self.__arr[i]
        self.__arr = new_arr
        self.__capacity = new_size

    def at(self, index):
        if index < 0 or index >= self.__size:
            raise IndexError("index out of range")
        return self.__arr[index]

    def clear(self):
        self.__arr = [None] * self.__capacity
        self.__size = 0

    def insert(self, index, value):
        if index < 0 or index > self.__size:
            raise IndexError("index out of range")
        if self.__size == self.__capacity:
            self.__resize(self.__capacity * 2)
        for i in range(self.__size, index, -1):
            self.__arr[i] = self.__arr[i - 1]
        self.__arr[index] = value
        self.__size += 1

    def erase(self, index):
        if index < 0 or index >= self.__size:
            raise IndexError("index out of range")
        if self.__size == 0:
            raise IndexError("erase from empty array")
        for i in range(index, self.__size - 1):
            self.__arr[i] = self.__arr[i + 1]
        self.__size -= 1
        self.__arr[self.__size] = None

    def __repr__(self):
        return f'DynamicArray({[self.__arr[i] for i in range(self.__size)]})'
    
    
arr = DynamicArray()

for i in range(15):
    arr.push_back(i)
print("After push_back 0-14:", arr)
print("Size:", arr.size())
print("Capacity:", arr.capacity())

arr.pop_back()
arr.pop_back()
print("After popping 2 elements:", arr)
print("Size:", arr.size())

arr.insert(5, 999)
print("After inserting 999 at index 5:", arr)

arr.erase(5)
print("After erasing index 5:", arr)

arr.clear()
print("After clear():", arr)
print("Size:", arr.size(), "Capacity:", arr.capacity())
