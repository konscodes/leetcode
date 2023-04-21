'''
Given an array of integers nums, calculate the pivot index of this array.

1. We could loop over each element and sum the elements to the right and to the left
- this approach will take too many itterations
2. Better way is to split the len in half and sum both sides
- then split the higher sum range in half and sum both sides
- repeat the split until the pivot is found
???
'''


def pivot(array: list) -> int:
    sum_left = [sum(array[:index]) for index, _ in enumerate(array)]
    sum_right = [sum(array[index + 1:]) for index, _ in enumerate(array)]
    for index, element in enumerate(sum_right):
        try:
            if sum_left.index(element) == index:
                return index
        except ValueError:
            pass
    return -1


if __name__ == '__main__':
    print(pivot([1, 7, 3, 6, 5, 6]))
