# 19)How Do You Handle Exceptions With Try/Except/Finally In Python? 
#Explain with coding snippets. 

try:
    a=int(input("Enter A:-"))
    b=int(input("Enter B:-"))
    print("Sum:-",a+b)
except Exception as e:
    print(e)
finally:
    print("This is Finally Block!")
    print("Mul:-",a*b)