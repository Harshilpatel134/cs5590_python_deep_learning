st=input("enter the string")
l=list(st)
c=0
d=0
for x in l:
    if(x.isdigit()):
       d=d+1
    if (x.isalpha()):
        c =c +1
print("digit:" + str(d) + " char:" + str(c))




