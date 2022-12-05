# 2.1  Longest Uncommon Subsequence I
# Given two strings a and b, return the length of the longest uncommon subsequence between a and b.
# If the longest uncommon subsequence does not exist, return -1.
# An uncommon subsequence between two strings is a string that is a subsequence of one but not the other.
# A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.
def find_lus_length(a: str, b: str):
    count = 0
    if a == b:
        return -1
    else:
        if len(a) >= len(b):
            return len(a)
        else:
            return len(b)

print(find_lus_length('hfmezmg', 'kgfqfeenshfw'))