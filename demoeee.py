# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("jatin satani", 36)

# print(p1.name,p1.age)
# print(p1.age,p1.name)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"    

# p1 = Person("John", 36)

# print(p1)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is","& " + self.name ,"My Age is :",self.age)

p1 = Person("jatin",36)
p1.myfunc()