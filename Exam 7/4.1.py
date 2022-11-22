def gcd_pro_max_2(* nums):
    nums = sorted(nums, reverse=True)
    if len(set(nums)) == 1:
        return (set(nums)).pop()
    for i in range(len(nums)-1):
        if nums[i] % nums[i+1] == 0:
            nums[i] = nums[i+1]
        else:
            nums[i] = nums[i] % nums[i+1]
    return gcd_pro_max_2(* nums)

print(gcd_pro_max_2(999,1999,2999,3999,4999))

def gcd_pro_max_1(* nums):
    while len(set(nums)) > 1:
        nums = sorted(nums, reverse=True)
        #print(nums)
        for i in range(0, len(nums) - 1):
            if nums[i] % nums[i + 1] == 0:
                nums[i] = nums[i + 1]
            else:
                nums[i] = nums[i] % nums[i + 1]
    print(set(nums).pop())

gcd_pro_max_1(999,1999,2999,3999,4999)