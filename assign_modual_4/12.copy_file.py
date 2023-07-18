# 12) Write a Python program to copy the contents of a file to another file.

fl=open('std.txt','a')

fl.write("Hi....")
fl.write("\n My Name Is Sanjay")
fl.write("\n I From DevBhumiDwarka")
fl.write("\n My Hobbie Is Playing Cricket")
fl.write("\n I love to Traveling")
fl.close()

fl=open('std.txt','r+')
d=open('st.txt','a')
d.write(fl.read())