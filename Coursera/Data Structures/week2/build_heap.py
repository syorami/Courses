# python3

from math import *

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
    # The following naive implementation just sorts
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap,
    # but in the worst case gives a quadratic number of swaps.

    LEN = len(self._data)
    for i in range(LEN // 2, -1, -1):
      parent = i
      while parent * 2 < LEN:
        idx = parent
        leftchild, rightchild = 2 * parent + 1, 2 * parent + 2
        if leftchild <= LEN - 1 and self._data[idx] > self._data[leftchild]: idx = leftchild
        if rightchild <= LEN - 1 and self._data[idx] > self._data[rightchild]: idx = rightchild

        if idx != parent:
          self._swaps.append([parent, idx])
          self._data[parent], self._data[idx] = self._data[idx], self._data[parent]
          parent = idx
        else:
          break

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
