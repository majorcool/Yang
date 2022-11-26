# You are given two non-negative integers num1 and num2.
# In one operation, if num1 >= num2, you must subtract num2 from num1, otherwise subtract num1 from num2.
def count_operations(count, num1: int, num2: int):
    if num1 == 0 or num2 == 0:
        return count
    if num1 > num2:
        count += 1
        num1 = num1 - num2
        return count_operations(count, num1, num2)
    elif num1 < num2:
        count += 1
        num2 = num2 - num1
        return count_operations(count, num1, num2)
    else:
        count += 1
        num1 = num1 - num2
        return count_operations(count, num1, num2)


try:
    print(count_operations(0, 4, 3))

except Exception as a:
    print(a)
