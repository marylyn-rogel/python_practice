class Dog: 
    """Practice: Modeling a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
         """Simulate a rolling over in response to a command"""
         print(f"{self.name} is rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

#My dog
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

#Your Dog
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")