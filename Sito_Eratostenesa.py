n=100
pierwsze=[]

for i in range(2,n+1):
    pierwsze.append(i)

print(pierwsze)
d=2

while d * d <= n:
    for i in range(d, (n // d) + 1):
        if (i * d) in pierwsze:
            pierwsze.remove(i * d)

    d = min([num for num in pierwsze if num > d])

print(pierwsze)