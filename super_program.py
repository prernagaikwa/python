class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name, self.age)


class student(person):
    def __init__(self,name,age,dob):
        self.sname=name
        self.sage=age
        self.dob=dob

        super().__init__("rahul",age)

    def displayinfo(self):
        print(self.sname,self.sage,self.dob)


oj=student("asma",65,"13-12-2003")
oj.display()
oj.displayinfo()

o1=person("ak",15)
o1.display()
