__version__ = '2.0.0p3'

from collections import deque


class RingBuffer(deque):
    def __init__(self, size_max):
        deque.__init__(self)
        self.size_max = size_max

    def _full_append(self, datum):
        deque.append(self, datum)
        self.popleft()

    def append(self, datum):
        deque.append(self, datum)
        if len(self) == self.size_max:
            self.append = self._full_append

    def tolist(self):
        return list(self)
