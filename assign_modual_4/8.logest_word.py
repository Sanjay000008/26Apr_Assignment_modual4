# 8) Write a python program to find the longest words

fl=open('std.txt','a')

fl.write("Hi....")
fl.write("\n My Name Is Sanjay")
fl.write("\n I From DevBhumiDwarka")
fl.write("\n My Hobbie Is Playing Cricket")
fl.write("\n I love to Traveling")
fl.close()

fl=open('std.txt','r+')
lw=fl.read().split()
lnw=len(max(lw, key=len))
result=[textword for textword in lw if len(textword) == lnw]
print(result)