# Given an integer array nums,
# return the largest perimeter of a triangle
# with a non-zero area, formed from three of these lengths.
# If it is impossible to form any triangle of a non-zero area, return 0.
def largest_perimeter(nums: list):
    nums = sorted(nums, reverse=True)
    for i in range(0, len(nums)-2):
        if nums[i + 1] +nums[i + 2] > nums[i]:
            return nums[i] + nums[1+i] + nums[2+i]
    else:
        return 0


print(largest_perimeter([1,1,2]))
print(largest_perimeter([2,1,2]))
print(largest_perimeter([2,1,5,6,9,10,13,7,7,3,2,5,4]))

