def find_shortest_subarray(nums: list[int]):
    long = len(nums)
    judge = list(set(nums))
    remain = 0
    num1 = []
    counts_list = []
    for i in judge:
        count = 0
        for q in nums:
            if i == q:
                count += 1
        if count > remain:
            remain = count
            num1 = [i]
        elif count == remain:
            num1.append(i)

    for num in num1:
        counts = 0
        for steps in nums:
            if steps != num:
                counts += 1
            else:
                break
        nums = nums[::-1]
        for steps in nums:
            if steps != num:
                counts += 1
            else:
                break
        counts_list.append(long - counts)
    counts_list = sorted(counts_list, reverse=False)
    return counts_list[0]


with open('2.2test.py', 'r') as f:
    for line in f.readlines():
        _ = line.split(' ')
        result = _.pop()[:-1:]
        __ = _[0].split(',')
        if int(find_shortest_subarray(__)) == int(result):
            print(True)
        else:
            print('False:{}'.format(line))
