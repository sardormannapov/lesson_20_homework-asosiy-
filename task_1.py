class Person_compare:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, other):
        if self.age < other.age:
            return f"{other.name} is older than me"

        elif self.age > other.age:
            return f"{other.name} is younger than me"

        elif self.age == other.age:
            return f"same age"


p1 = Person_compare("Samuel", 24)
p2 = Person_compare("Joel", 36)
p3 = Person_compare("Lily", 24)

print(p1.compare_age(p2))
print(p2.compare_age(p1))
print(p1.compare_age(p3))
