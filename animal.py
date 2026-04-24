class Animal:
    """
    Base class representing a generic animal.
    """
    kingdom = "Animalia"
    all_animals = []  # Class variable to track all animals

    # object specific attributes
    def __init__(self, name, species):
        self.name = name
        self.species = species
        Animal.all_animals.append(self)  # Add each new animal to the list

    def speak(self):
        print(f"The animal makes a noise.")

    def __str__(self):
        return f"Kingdom: '{self.kingdom}', Name: '{self.name}', Species: '{self.species}'"
 
