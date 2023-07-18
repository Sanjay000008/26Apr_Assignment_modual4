# 15) When will the else part of try-except-else be executed
"""
  If there is no exception then this block will be executed
"""

try:
    a=int(input("Enter A:-"))
    b=int(input("Enter B:-"))
    print("Sum:-",a+b)
except Exception as e:
    print(e)
else:
    print("This is Finally Block!")
    print("Mul:-",a*b)