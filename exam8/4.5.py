# Given an integer array nums,
# return the largest perimeter of a triangle
# with a non-zero area, formed from three of these lengths.
# If it is impossible to form any triangle of a non-zero area, return 0.
def largest_perimeter(nums: list):
    if nums[0] + nums[1] > nums[2] and nums[1] + nums[2] > nums[0] and nums[0] + nums[2] > nums[1]:
        return nums[0] + nums[1] + nums[2]
    else:
        return 0


print(largest_perimeter([2,1,2]))
print(largest_perimeter([1,2,1]))

