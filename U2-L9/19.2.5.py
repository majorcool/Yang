# 19.2.5  Sum of Unique Elements
# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
# Return the sum of all the unique elements of nums.
def sum_of_unique(nums: list[int]):
    repeat = []
    sum = 0
    for i in range(0, len(nums)):
        for q in range(i+1, len(nums)):
            if nums[i] == nums[q]:
                repeat.append(nums[i])
                repeat.append(nums[q])
                repeat = list(set(repeat))
    nums = list(set(nums))
    for i in repeat:
        nums.remove(i)
    for i in nums:
        sum += i
    return sum


try:
    print(sum_of_unique([1,2,3,4,5]))

except Exception as a:
    print(a)
