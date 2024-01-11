class Animal:
    def speak(self):
        print("AnimalSpeaking")
    
    def wash(self):
         print("wash")

class Dog(Animal):
    def bark(self):
        print("dog barking")

class DogChild(Dog):
   def eat(self):
        print("Eating bread...")
        
d=DogChild()
d.bark()
d.speak()
d.wash()
d.eat()
