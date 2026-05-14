
# Example of a simple class & object creation

class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"
    
obj = MyClass("Akash")
print(obj.greet())


# --- IGNORE ---
# Example without __init__ method

class Myclassnt:
    def greet(self,name):
        print(f"Hello, {name}!")
    
objnt = Myclassnt()
objnt.greet("Sneha-Tanamay")


# Modify properties of class object
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("AKash", 21)

p1.age = 22

print(p1.age)