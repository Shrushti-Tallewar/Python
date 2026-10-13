s = "anagram"
t = "nagaram"

if len(s)!= len(t):
      print("False")
else:
    for el in s:
        if s.count(el)== t.count(el): 
            
             print("True")
             break
        else:
            print("False")