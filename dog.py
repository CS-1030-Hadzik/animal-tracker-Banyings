from animal import Animal

class Dog(Animal):
    """
    Derived class representing a dog, which is a type of Animal.
    """
    # Initialize the Dog class and add the breed attribute.
    # The constructor should accept name, species, and breed as parameters.
    def __init__(self, name, species, breed):
        super().__init__(name, species)  # Call the parent class constructor
        self.breed = breed

    # Override the __str__ method to include the breed.
    def __str__(self):
        return f"Kingdom: '{self.kingdom}', Name: '{self.name}', Species: '{self.species}', Breed: '{self.breed}'"

    # Add a method for the dog to make a specific sound.
    def speak(self):
        print("The dog barks.")
    