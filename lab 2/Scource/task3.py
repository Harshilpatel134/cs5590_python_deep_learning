'''  library management system '''
class people:
    def __init__(self,n=None,a=None,e=None):
        self.name=n
        self.age=a
        self.email=e
    def show(self):
        print("name:" + self.name)
        print("age:" + str(self.age))
        print("email:" + self.email)
class student(people):
    def __init__(self,p=None,a=None,e=None,i=None):
        if(type(p)!=people):
            super().__init__(p,a,e)
            self.student_id=i
        else:
            super().__init__(p.name, p.age, p.email)
            self.student_id = a
    def show(self):
        print("Student id:" + str(self.student_id))
        super().show()
class empoyee():
    def __init__(self,i,s):
        self.employee_id=i
        self.salary=s
    def show(self):
        print("emp id:"+ str(self.employee_id))
        print("salary:"+ str(self.salary))
class librarystaff(people,empoyee):
    def __init__(self,n=None,a=None,e=None,i=None,s=None):
        super().__init__(n,a,e)
        self.employee_id=i
        self.salary=s
    def show(self):
        #print("A id:" + str(self.author_id))
        super().show()
        empoyee.show(self)
class author(people):
    def __init__(self,n=None,a=None,e=None,i=None):
        super().__init__(n, a, e)
        self.author_id = i
    def show(self):
        print("Author id:" + str(self.author_id))
        super().show()

class book():
    def __init__(self,i=None,t=None,a=None,ty=None):
        self.book_id=i
        self.book_title=t
        self.book_author=a
        self.book_type=ty
    def show(self):
        print("book id:" + str(self.book_id))
        print("book title:" + self.book_title)
        print("book author:" + self.book_author.name)
        print("book type:" + self.book_type)
## creating temp people class object
print("------------------STudent------------------")
a=people("harshil",22,"harshilpatel002@gmail.com")
a.show()                                                         ## diaplay detail of people
## creating first student with detail from temp people created
## i have implemented constructor overloading by my code which is not supported by python
s=student(a.name,a.age,a.email,"s01")
s2=student(a,"s02")
s2.show()
s.show()
## creating  temp empoyee
print("------------------empoyee------------------")
e=empoyee("e01",2000)
e.show()
## creating librarystaff which have multiple inheritance from people class and empoyee class
l=librarystaff("king",22,"dasas","e02",3000)
l.show()
print("-----------------book----------------------")
## creating author and book
at=author("harshil",23,"harshil@af.com","a01")
b=book("b01","python",at,"educational")
b.show()