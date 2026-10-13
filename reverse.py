# REVERSE AN INTEGER
# s = 1234
# rev = 0
# while s > 0:
#      r = s % 10
#      rev = rev * 10 + r
#      s // 10 
# print(rev)

# REVERSE A STRING
# s ="mango"
# print(s[::-1])

# OR

s = "mango"
i = len(s)-1
rev =""
while i >= 0:
    rev = rev + s[i]
    i-=1
print(rev)

