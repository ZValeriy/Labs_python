def findmin(list):
    minind = list[0]
    for i in range(1, len(list) - 1):
        if list[i] < minind:
            minind = list[i]
    return minind


def findcount(list):
    summ = 0
    for i in list:
        summ += i
    return summ / len(list)


arr = list(map(int, input().split()))

print(*arr)
print(findmin(arr))
print(findcount(arr))




