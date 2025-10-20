n,m,k=map(int,input().split())
if n >= m and n >= k:
    print(n)
elif m >= n and m >= k:
    print(m)
else:
    print(k)