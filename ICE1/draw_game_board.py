h=int(input("enetr height:"))
w=int(input("enetr width:"))
l=[" "]*(h*2)

for i in range(0,h):

    for x in range(0,w):
        l[i*2]+= str(" ---")
        l[(i*2)+1]+= str("|   ")
    l[(i * 2) + 1] += str("|")
temp=" "
for j in range(0,w):
    temp+=str(" ---")
l=l+[temp]

for x in l:
    print(x)

