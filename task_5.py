inp = input("enter employee: ")
class Person:
    def __init__(self, name, username, inp):
        self.name = name
        self.username = username
        self.input = inp

    def fullname(self):
        return f"{self.name} {self.username}"

    def email(self):
        return f"{self.name}.{self.username}@company.com"

    def firstname(self):
        return f"{self.name}"



obj = Person("Sardor", "Mannapov", inp=inp)
if inp == "fullname":
    print(obj.fullname())

elif inp == "email":
    print(obj.email())

elif inp == "firstname":
    print(obj.firstname())
