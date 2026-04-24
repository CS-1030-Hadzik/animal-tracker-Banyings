from animal import Animal
from dog import Dog


if __name__ == "__main__":

    dog1 = Animal("Fido", "Canine")
    dog2 = Animal("Nala", "Canine")

    print(dog1)
    dog1.speak()

    print(dog2)
    dog2.speak()

    # Create an instance of the Animal class
    generic_animal = Animal("Generic Animal", "Unknown")
    # Print the Animal instance
    print(generic_animal)
    # Call the method to make a generic animal sound
    generic_animal.speak()

    # Create an instance of the Dog class
    my_dog = Dog("Rex", "Canine", "German Shepherd")
    # Print the Dog instance
    print(my_dog)
    # Call the method to make the dog-specific sound
    my_dog.speak()

    # Print out all the animals
    print("\nAll animals:")
    for animal in Animal.all_animals:
        print(animal)