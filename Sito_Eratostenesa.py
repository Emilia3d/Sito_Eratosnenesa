n=100
pierwsze=[]

for i in range(2,n+1):
    pierwsze.append(i)

print(pierwsze)
d=2

while d * d <= n:
    i = d
    while i * d <= n:
        if i * d in pierwsze:
            pierwsze.remove(i * d)
        i += 1

    # Znajdujemy najmniejszy element listy większy od d
    for num in pierwsze:
        if num > d:
            d = num
            break

print(pierwsze)