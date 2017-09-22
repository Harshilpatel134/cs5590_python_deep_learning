st=input("enter the string:")
l=st.split(" ")    ## it will split input string and store it in list
s=set(l)            ## converting list in set to remove duplication
l1=list(s)          ##converting set into list
l1.sort()           ## apply sorting on list
ans=""
for x in l1:        ##this for loop is to make the output string
    ans+=x+" "
print(ans)