d = {'gfg' : [5,6,7,8],' is' : [10,11,7,5], 'best' : [6,12,10,8], 'for' : [1,2,5]}
res = list(sorted({ele for val in d.values() for ele in val}))
print(res)