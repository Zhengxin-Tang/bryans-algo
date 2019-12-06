from nn.Student import Student
from nn.SortTestHelper import *


def selection_sort(arr):
    length = len(arr)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == '__main__':
    a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    selection_sort(a)
    for i in range(10):
        print(a[i], " ", end="")
    print("")

    b = [5.5, 4.4, 3.3, 2.2, 1.1]
    selection_sort(b)
    for i in range(5):
        print(b[i], " ", end="")
    print("")

    c = ["D", "C", "B", "A"]
    selection_sort(b)
    for i in range(4):
        print(c[i], " ", end="")
    print("")

    d = [Student("D", 90), Student("C", 100), Student("B", 95), Student("A", 95)]
    selection_sort(d)
    for i in range(4):
        print(d[i], " ", end="")
    print("")

    n = 10000
    random_list = generate_random_array(n, 0, n)
    test_sort("Selection Sort: ", selection_sort, random_list)
