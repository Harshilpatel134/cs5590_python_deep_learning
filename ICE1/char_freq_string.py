st=input("enter the string")
l=list(st)
ln=[]
lc=[]
for x in l:
    f=0
    for h in ln:
        if(h==x):
            lc[ln.index(x)] = lc[ln.index(x)] + 1
            f=1
            break
    if f==0:
        ln.append(x)
        lc.append(1)
for x in range(0, len(ln)):
    print(ln[x] + "    "+ str(lc[x]))

