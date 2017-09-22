no=int(input("enter the number:"))
d1={}                             ## creating empty dictionary
for x in range(1,no+1):            ## running for loop from 1 to the given number
    d1.update({x:x*x})                  ## storing data in dictionary
print(d1)                           ## output result
