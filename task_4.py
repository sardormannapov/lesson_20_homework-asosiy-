inp = input("enter about football player: ")

class Futbol_player:


    def __init__(self, name, age, height, weight, inp):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.input = inp

    def get_name_age(self):
        return f"{self.name} is age {self.age}"

    def get_height(self):
        return f"{self.name} is {self.height}"

    def get_weight(self):
        return f"{self.name} weighs {self.weight}kg"



obj = Futbol_player(name="David Jones", age=25, height=175, weight=75, inp=inp)
if inp == "get_age":
    print(obj.get_name_age())

elif inp == "get_height":
    print(obj.get_weight())

elif inp == "get_weight":
    print(obj.get_weight())
