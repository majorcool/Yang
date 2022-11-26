# 19.2.4  Counting Words With a Given Prefix
# You are given a list of string words and a string pref.
# Return the number of strings in words that contain pref as a prefix.
# A prefix of a string s is any leading contiguous substring of s.
def prefix_count(words: list[str], pref: str):
    len_pref = len(pref)
    count = 0
    for i in words:
        if pref == i[:len_pref:]:
            count += 1
    return count


try:
    print(prefix_count(['at', '2'], 'at'))

except Exception as result:
    print(result)
