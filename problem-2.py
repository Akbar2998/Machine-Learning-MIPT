N = int(input())
b = []
indexlar_massa = []
massa = []
v = []
cordinata = []
for i in range(N):
    x = input().split()
    b.append(x)
for i in range(N):
    massa.append(b[i][1])
    v.append(b[i][1])
    cordinata.append(b[i][0])
massa.sort(reverse = True)
for i in range(N):
    for j in range(N):
        if massa[i] == v[j]:
            indexlar_massa.append(j)
#print(b)
#print(massa)
#print(indexlar_massa)
for i in range(N):
    print(cordinata[indexlar_massa[i]])
