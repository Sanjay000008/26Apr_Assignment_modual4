#29)What relationship is appropriate for Student and Person?

"""
    In object-orianted programming,inheritance is the mechanism of basing an object or class
    upon another object or class,ratining similar implimantation.

    Simply we can say that it establishes an "is-a" or "Kind of" ralationship between Student
    and Person class.Saying that,Student is a kind of Person.
"""

class person:
    sid=0
    sname=""
    def getdata(self):
        self.sid=int(input("Enter Your Id:-"))
        self.sname=input("Enter Your Name:-")
        print("ID:-",self.sid)
        print("Name:-",self.sname)

class student(person):
    def getdata(self):
        return super().getdata()
    
pr=person()
pr.getdata()
st=student()
st.getdata()