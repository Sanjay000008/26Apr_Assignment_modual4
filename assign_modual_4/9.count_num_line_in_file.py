# 9)Write a Python program to count the number of lines in a text file


fl=open('std.txt','a')

fl.write("Hi....")
fl.write("\n My Name Is Sanjay")
fl.write("\n I From DevBhumiDwarka")
fl.write("\n My Hobbie Is Playing Cricket")
fl.write("\n I love to Traveling")
fl.close()

fl=open('std.txt','r+')
n=0
for i in fl:
    n +=1
print("Number Of Line :-",n)