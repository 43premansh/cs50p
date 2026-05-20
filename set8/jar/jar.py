class Jar:
    def __init__(self, capacity=12):
        if capacity <= 0 :
            raise ValueError("negative cant fit the jar dude!!")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if (self._size + n) > self.capacity :
            raise ValueError("cant fill that much dude!")
        self._size += n

    def withdraw(self, n):
        if (self._size - n) < 0 :
            raise ValueError("cant borrow that much hehe")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size