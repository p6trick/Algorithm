def exchange(S):
    n = len(S)

    for i in range(n-1):
        for j in range(i+1,n):
            if S[i]>S[j]:
                S[i],S[j] = S[j],S[i]
    return S

S = [5,2,4,1,3]

print(S)
print(f'after exchange : {exchange(S)}')