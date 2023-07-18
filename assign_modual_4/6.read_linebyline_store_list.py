# 6) Write a Python program to read a file line by line and store it into a list
fl=open('std.txt','a')

fl.write("Hi....")
fl.write("\n My Name Is Sanjay")
fl.write("\n I From DevBhumiDwarka")
fl.write("\n My Hobbie Is Playing Cricket")
fl.write("\n I love to Traveling")
fl.close()

print("------------------------------")
fl=open('std.txt','r+')
print(fl.read())
fl.close()
print("--------------------------------------------")
fl=open('std.txt','r+')
print(fl.readlines())