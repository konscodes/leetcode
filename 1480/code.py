'''
Running sum for each element will be a sum of elements before it.
If the len of the list is 4 then sum of all list elements will be sum(nums[0:4]).
At the same time the id of the last element in the list is 3
So running sum for each element id will be sum(nums[0:(id + 1)])
'''


def runningSum(nums: list[int]) -> list[int]:
    result = [0] * len(nums)
    for id, number in enumerate(nums):
        result[id] = sum(nums[0:(id + 1)])
    return result


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(runningSum(nums))
