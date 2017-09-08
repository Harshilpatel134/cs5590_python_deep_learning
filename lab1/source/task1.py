with open('text.txt') as f:
    lines = f.read().split(" ")
ln=[]
lc=[]
for x in lines:
    f=0
    for h in ln:
        if(h==x):
            lc[ln.index(x)] = lc[ln.index(x)] + 1
            f=1
            break
    if f==0:
        ln.append(x)
        lc.append(1)
f = open('output.txt', 'w')
for x in range(0,len(ln)):
    print(ln[x] + "    "+ str(lc[x]))
    f.write(ln[x] + "    "+ str(lc[x]) + "\n")
f.close()


