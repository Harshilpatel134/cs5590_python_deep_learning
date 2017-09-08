st=input("enter the string:")
for x in range(ord('a'), ord('z')+1):
    if st.find(chr(x))==-1:
        print("string do not contain all a-z")
        exit(0)
print("string contain all a-z")

