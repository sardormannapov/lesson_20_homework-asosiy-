inp = input("enter name: ")
class Person:
    def __init__(self, fname, lname, fullname, initials, inp):
        self.fname = fname
        self.lname = lname
        self.fullname = fullname
        self.initials = initials
        self.input = inp

    def first_name(self):
        return f"{self.fname}"

    def last_name(self):
        return f"{self.lname}"

    def full_name(self):
        return f"{self.fname} {self.lname}"

    def short_forms(self):
        return f"{self.initials}"


obj = Person("Sardor", "Mannapov", "Sardor Mannapov", "S.M", inp=inp)
if inp == "fname":
    print(obj.fname())

elif inp == "lname":
    print(obj.lname())

elif inp == "fullname":
    print(obj.fullname())

elif inp == "initials":
    print(obj.initials())

else:
    print("error")