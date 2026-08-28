def fun(p, t, r):
    return (p * t * r) / 100

p = int(input("Entre the principle:"))
t = int(input("time:"))
r = int(input("Rate of interest:"))

res = fun(p, t, r)
print(res)