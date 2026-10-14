s = "leetcode"
found = False
for ch in s:
    if s.count (ch)== 1 :
        print(s.index(ch))
        found = True
        break
if found == False:
    print(-1) 
