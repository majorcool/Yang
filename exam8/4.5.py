# Given an integer array nums,
# return the largest perimeter of a triangle
# with a non-zero area, formed from three of these lengths.
# If it is impossible to form any triangle of a non-zero area, return 0.
def triangle(nums:list):
    for i in range(0, len(nums)):
        for q in range(i + 1, len(nums)):
            other = nums.remove()

