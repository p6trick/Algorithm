def binarysearch(S,x):
    low = 0
    high = len(S) - 1
    location = -1

    while(low <= high and location == -1):
        mid = (low + high) // 2
        if x == S[mid]:
            location = mid
        elif x < S[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return location

S = [0,1,2,3,4,5,6,7,8]
x1 = 2
x2 = 9
print(S)
print(f'x1 : {binarysearch(S, x1)}')
print(f'x2 : {binarysearch(S, x2)}')