def findmin(list):
    return min(list)


def findcount(list):
    return sum(arr)/len(arr)


arr = list(map(int, input().split()))

print(*arr)
print(findmin(arr))
print(findcount(arr))




