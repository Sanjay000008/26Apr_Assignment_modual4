# 22) How to Define a Class in Python? What Is Self? Give An Example Of A Python Class

"""
Class:-
    A class in Python can be defined using the class keyword. As per the syntex above,a class is defined
    using the class keyword followed by the class name and: operator after the class name,which allows
    you to coiuntinue in the next indented line to define class members.

SELF:-
    Self represents the instance of class.This handy keyword allows you to access variables,
    attributes,and methods of a defined class in Python.The self parameter doesn't have to be 
    named "self" as you can call it by any other
"""

class student:
    sid=8
    snm='Madhav'

    def gd(self):
        print("ID:-",self.sid)
        print("Name:-",self.snm)

st=student()
st.gd()