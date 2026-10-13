# s = "madam"
# rev = 0
# while s > 0:
#      r = s % 10
#      rev = rev * 10 + r
#      s // 10 
# print(rev)

s = "car"
p =s[::-1]

if p == s:
    print("true")
else:
    print("false")