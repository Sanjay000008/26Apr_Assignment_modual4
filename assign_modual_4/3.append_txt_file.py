# 3)Write a Python program to append text to a file and display the text

fl=open('text.txt','a+')
fl.write("hi..! This is my Fisrt File program in Python")
fl.write("\nMy Name Is Snajay")
fl.write("\nHow Are You?")
fl.close()
print("--------------------------------")
print("This Is Your Data")
fl=open('text.txt','r+')
print(fl.read())