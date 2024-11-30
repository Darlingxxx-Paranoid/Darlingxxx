#快速排序
import typing
from typing import List
from typing import Tuple
class QuickSort:
    def __init__(self):
        pass
    def quicksort(self, arr: List[int]):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle:List[int] = [x for x in arr if x == pivot]
        right:List[int] = [x for x in arr if x > pivot]
        return self.quicksort(left) + middle + self.quicksort(right)

#全局变量 arr:List[int]
arr: typing.List[int] = []

def main():
    n = input()
    n:int = int(n)
    global arr
    for i in range(n):
        arr.append(int(input())) #输入n个数
    qs = QuickSort()
    arr = qs.quicksort(arr)
    print(arr)

if __name__ == '__main__':
    main()