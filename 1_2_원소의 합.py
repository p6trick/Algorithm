def sum(S):
    n = len(S)
    result = 0
    for i in range(1,n):
        result += S[i]
    return result

S = [-1, 1,2,3,4,5]

print(S)
print(f'sum : {sum(S)}')