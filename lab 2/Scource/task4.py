import numpy
l=[]
a=1
d=input("enter dimension 1, 2, 3:")   ## geting no. of dimension from user
for i in range(0,int(d)):               ## getting size of each dimension
    l+=[int(input("enter size of "+ str(i+1) +" dimension:"))]
    a=a*l[i]
l.reverse()
arr=numpy.random.randint(0,1000,a,int)   ## creating random value in vector
arrr=arr.reshape(l)                         ## reshaping it to our requirement
print (arrr)                                ## printing vector
print ("max element in vector is:" + str(numpy.amax(arrr)))   ## printing max element
print("it has been replaced with 100")