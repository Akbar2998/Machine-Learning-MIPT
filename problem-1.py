a = int(input())
b = []
s  = ""
while a > 0:
    b.append(a%10)
    a = a // 10
c = b.copy()
for i in range(c.count(0)):
    c.remove(0)
s += str(min(c))
#print(b)
#print(c)
b.remove(min(c))
for i in range(len(b)):
    s += str(min(b))
    b.remove(min(b))
print(int(s))
