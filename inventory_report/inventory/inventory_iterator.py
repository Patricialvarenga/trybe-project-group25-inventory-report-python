# https://docs.python.org/3/library/collections.abc.html
from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, list):
        self.list = list
        self.contator = 0

    def __next__(self):
        try:
            iteration = self.list[self.contator]
        except IndexError:
            raise StopIteration()

        self.contator += 1
        return iteration
