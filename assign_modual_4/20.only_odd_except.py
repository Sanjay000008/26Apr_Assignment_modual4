# 20) Write python program that user to enter only odd numbers, else will raise an exception

try:
    n=int(input("Enter Number:-"))
    mod = n % 2
    if mod > 0:
        print("This is an odd Number")
    else:
        print("This is Even Number")
except:
    pass

