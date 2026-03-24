class Animal:
    """
    Base class representing a generic animal.
    """
    kingdom = "Animalia"

    #object specific attributes
    def __init__(self, name, species): # 
        self.name = name
        self.species = species

    def speak(self):
        print (f"{self.name} makes a noise")

    def __str__(self):
        return (f"Kingdom: {self.kingdom}\n"
                f"Name: {self.name}\n"
                f"Species: {self.species}\n")
 
