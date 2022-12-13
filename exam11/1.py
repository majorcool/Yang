def longest_common_prefix(strs: list[str]):
    judge = str(strs[0])
    for i in range(1, len(strs)-1):
        if len(judge) >= len(strs[i]):
            count = len(strs[i])
        else:
            count = len(judge)
        for q in range(0, count):
            if strs[i][q] != judge[q]:
                judge = judge[:q:]
                break
    return judge


with open('1.1test.py', 'r') as f:
    for line in f.readlines():
        _ = line.split(' ')
        result = _.pop()[:-1:]
        __ = _[0].split(',')
        if longest_common_prefix(__) == result:
            print(True)
        else:
            print('False:{}'.format(line))