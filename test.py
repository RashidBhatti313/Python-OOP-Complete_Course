class Person: # making class of person
    # init method or constructor
    def __init__(self,name, age,gender) -> None:
        # instance variable set 
        self.name = name
        self.age = age
        self.gender = gender

    # def show (self):
    #     return f" name : {self.name} age = {self.age} \n gender = {self.gender}"
    def __str__(self):

        return f" name : {self.name}\n age = {self.age} \n gender = {self.gender}"
#creating object of this class


p1 = Person("ali",33,"Male")

p2 = Person("Rashid",18,"Male")

p3 = Person("Chacha",19,"Male")

p4 = Person("Sami",17,"Male")
# print(p1.show())
# print(p2.show())
# print(p3.show())
# p4.show()
print(p1)
