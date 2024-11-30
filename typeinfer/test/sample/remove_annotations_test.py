import typing
from typing import List
from typing import Tuple


class QuickSort:

    def __init__(self):
        pass

    def quicksort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quicksort(left) + middle + self.quicksort(right)


arr = []


def main():
    n = input()
    n = int(n)
    global arr
    for i in range(n):
        arr.append(int(input()))
    qs = QuickSort()
    arr = qs.quicksort(arr)
    print(arr)


if __name__ == '__main__':
    main()
