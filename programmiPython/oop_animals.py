class Pet:
  def __init__(self, pet_type, name, sound):
    self.pet_type = pet_type
    self.name = name
    self.sound = sound

  def speak(self):
    print(f"{self.name} goes {self.sound}!")

  def play(self):
    print(f"{self.name} is playing!")

# inheritance (avoid repetitive code!)
class Cat(Pet):
  def __init__(self, name, sound, coat_length):
    super().__init__("cat", name, sound)
    self.coat_length = coat_length

# we use encapsulation to group together related data and methods   
  def purr(self):
    print(f"{self.name} is purring.")

class Dog(Pet):
  def __init__(self, name, sound, size):
    super().__init__("dog", name, sound)
    self.size = size

# polymorphism: we override a superclass method to customize the method's function within a subclass
  def speak(self):
    print(f"{self.name} the {self.size} dog goes {self.sound}!")
  
cat = Cat("Oscar", "Meow", "long")
cat.purr()
dog = Dog("Karl", "Woof", "big")