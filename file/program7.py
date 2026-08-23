series = list(map(int,input().split()))
print(series)


for i in range(len(series)):
    for j in range ( i +1 ,len(series)):
        if series[i]> series[j] :
            series[i],series[j]= series[j],series[i]

print(series)
