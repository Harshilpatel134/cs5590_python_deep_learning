import random
n2=random.randint(0, 9)
print(n2)
while(1):
    n=input("enter no. between 1-10:")
    n1=int(n)

    if n1==n2:
        print("ooo! u got it")
        exit(0)
    else:
        print("no try again")
