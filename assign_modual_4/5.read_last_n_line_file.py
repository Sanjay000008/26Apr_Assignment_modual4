# 5)Write a Python program to read last n lines of a file

fl=open('std.txt','a')

fl.write("Hi....")
fl.write("\n My Name Is Sanjay")
fl.write("\n I From DevBhumiDwarka")
fl.write("\n My Hobbie Is Playing Cricket")
fl.write("\n I love to Traveling")
fl.close()

print("------------------------------")
fl=open('std.txt','r+')
print(fl.readlines())