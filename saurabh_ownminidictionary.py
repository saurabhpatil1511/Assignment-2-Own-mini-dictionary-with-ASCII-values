# Program to print a dictionary whose keys  should be the alphabet from a-z and the values should be corresponding ASCII values
di={}
for i in range(97,123):
    di[chr(i)]=ord(chr(i))
print(di)
