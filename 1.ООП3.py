import math

class ValueList:
    def __init__(self):
        self._data = []
        self._sum = 0
        self._sum_squared = 0
        self._count = 0

    def _update_stats(self):
        self._count = len(self._data)
        if self._count > 0:
            self._avg = self._sum / self._count
            self._sd = math.sqrt((self._sum_squared / self._count) - (self._avg ** 2))
        else:
            self._avg = 0
            self._sd = 0

    def getElem(self, index):
        if 0 <= index < self._count:
            return self._data[index]
        raise IndexError("Index out of range.")

    def setElem(self, index, value):
        if 0 <= index < self._count:
            old_value = self._data[index]
            self._data[index] = value

            self._sum = self._sum - old_value + value
            self._sum_squared = self._sum_squared - (old_value ** 2) + (value ** 2)

            self._update_stats()
        else:
            raise IndexError("Index out of range.")

    def newElem(self, value):
        self._data.append(value)
        self._sum += value
        self._sum_squared += value ** 2
        self._update_stats()

    def getAvg(self):
        return self._avg

    def getSD(self):
        return self._sd
