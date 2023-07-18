# 10) Write a Python program to count the frequency of words in a file. 
from collections import Counter
fl=open('std.txt','a')

fl.write("Hi....")
fl.write("\n My Name Is Sanjay")
fl.write("\n I From DevBhumiDwarka")
fl.write("\n My Hobbie Is Playing Cricket")
fl.write("\n I love to Traveling")
fl.close()
def word_count(std):
    with open(std) as fl:
        return Counter(fl.read().split())
    
print("Number Of Word in the File:-",word_count("std.txt"))