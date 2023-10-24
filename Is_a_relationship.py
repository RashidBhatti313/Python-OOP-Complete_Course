# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def eat(self):
#         pass

#     def display(self):
#         return f" name of  animal {self.name} \n age = {self.age}"
#     def __str__(self):
#         return f" name of  animal {self.name} \n age = {self.age}"
    


# # a1 = Animal("Buldog",3)

# # print(a1)
# # print(a1.name, a1.age)

# # print(a1.display())
# class Carnivours(Animal):
#     def __init__(self, name, age):
#         super().__init__(name, age)

#     def eat(self):
#         return f" they eat meat"
    
#     def __str__(self):
#         return f"{super().__str__()} \n{self.eat()}"
    
# a2 = Carnivours("LOIN",3)
# print(a2.name)
# print(a2)

# class Herbivours(Animal):
#     def __init__(self, name, age):
#         super().__init__(name, age)

#     def eat(self):
#         return f" they eat Herb or vegitables"
    
#     def __str__(self):
#         return f"{super().__str__()} \n{self.eat()}"
    
# a3 = Herbivours("COW",12)
# print(a3)

# class Omnivours(Animal):
#     def __init__(self, name, age):
#         super().__init__(name, age)

#     def eat(self):
#         return f" they eat Herb or vegitables and meath both"
    
#     def __str__(self):
#         return f"{super().__str__()} \n{self.eat()}"
    
# a4 = Omnivours("Human", 22)
# print(a4)



class Animal:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def eat (self):
        pass

    def display(self):
        return f" name of animal = {self.name} \n age of animal = {self.age}"
    def __str__(self) -> str:
        return f" name of animal = {self.name} \n age of animal = {self.age}"
    
# a1 = Animal("Bulldog", 3)
# print(a1)
# print(a1.name, a1.age)
# print(a1.display())

class Carnivours(Animal):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)

    def eat(self):
        return f" They eat meat: "
    
    def __str__(self) -> str:
        return f"{super().__str__()} \n {self.eat()}"
    
# a2 = Carnivours("LOIN", 4)
# print(a2)

class Herbivours(Animal):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)

    def eat(self):
        return f" They eat Herb or Vegetables"
    
    def __str__(self) -> str:
        return f"{super().__str__()} \n {self.eat()}"
    
# a3 = Herbivours("COW", 11)
# print(a3)

class Omnivours(Carnivours,Herbivours):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
    def eat(self):
        return f" They eat Herb or vegetables: "
    
    def __str__(self) -> str:
        return super().__str__()
    
a4 = Omnivours("Human", 22)
print(a4)


# class Carnivours:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def __str__(self) -> str:
#         return f" Name of Dog: {self.name} \n Age of Dog: {self.age}"
    


