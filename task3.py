from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):
    """Abstract class representing a generic animal."""

    @abstractmethod
    def make_sound(self):
        """Abstract method that must be implemented by all subclasses."""
        pass

    def describe(self):
        """Concrete method that provides a general description."""
        print(f"I am a {self.__class__.__name__}.")

# Derived Classes
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

# Testing the Classes
if __name__ == "__main__":
    # Instantiate each subclass
    animals = [Dog(), Cat(), Cow()]

    # Call make_sound() and describe() for each animal
    for animal in animals:
        animal.describe()
        print(f"Sound: {animal.make_sound()}")
        print("-" * 30)
