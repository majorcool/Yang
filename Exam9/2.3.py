# 2.3  Find the Highest Altitude
# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip at point 0 with altitude equal to 0.
# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i and i + 1 for all (0 <= i < n).
# Return the highest altitude of a point.
def highest(n:list):
    altitudes = [0]
    for i in range(0, len(n)):
        altitudes.append(n[i]+altitudes[i])
    altitudes = sorted(altitudes, reverse=True)
    return altitudes[0]


print(highest([-5,1,5,0,-7]))