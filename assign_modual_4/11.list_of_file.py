# 11)Write a Python program to write a list to a file

d=[]
n=int(input("Enter Number Of list Data:-"))
for i in range(n):
    x=input("Enter Your Data:-")
    d.append(x)
print(d)
fl=open('d.txt','w')
for i in d:
    fl.write(i+"\n")

