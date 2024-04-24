n = 5  # Number of processes
m = 3  # Number of resources

alloc = [
    [0, 1, 0],
    [3, 0, 2],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

max_demand = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]

avail = [2, 3, 0]
f = [0] * n
ans = []
ind = 0

# Calculate need matrix
need = [[max_demand[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]

for k in range(n):
    for i in range(n):
        if f[i] == 0:
            flag = 0
            for j in range(m):
                if need[i][j] > avail[j]:
                    flag = 1
                    break
            if flag == 0:
                ans.append(i)
                for y in range(m):
                    avail[y] += alloc[i][y]
                f[i] = 1

flag = 1
for i in range(n):
    if f[i] == 0:
        flag = 0
        print("The following system is not safe")
        break

if flag == 1:
    print("Following is the SAFE Sequence")
    print("P" + " -> P".join(map(str, ans)))
