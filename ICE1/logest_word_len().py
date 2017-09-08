st=input("enter the list in one line with space:" )
l=st.split(" ")
max=0
for x in l:
    if len(x)>max:
        max=len(x)
print(max)