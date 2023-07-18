# 2) Write a Python program to read an entire text file

f=open("file.txt",'a+')

def gd():
    id=input("Enter ID:-")
    name=input("Enter Name:-")

    f.write(f"ID={id} \n Name={name}\n")

n=int(input("Enter Number Of Stident:-"))
for i in range(n):
    gd()
f.close()
print("--------------------------------")
f=open("file.txt",'r+')
print(f.read())