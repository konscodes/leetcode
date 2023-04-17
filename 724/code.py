'''
Given an array of integers nums, calculate the pivot index of this array.

1. We could loop over each element and sum the elements to the right and to the left
- this approach will take too many itterations
2. Better way is to split the len in half and sum both sides
- then split the higher sum range in half and sum both sides
- repeat the split until the pivot is found
???
'''
