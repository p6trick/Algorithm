def search(n,S,x):
    location = 0
    while(location<=n and S[location]!=x):
        location += 1

    if location > n:
        location = 0
    return location

S = [0,1,2,3,4,5]
n = 5
x1 = 3
x2 = 6

print(f'x1 = {x1} == {search(n,S,x1)}')
print(f'x2 = {x2} == {search(n,S,x2)}')