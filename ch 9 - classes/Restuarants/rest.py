class Resturant: 
    """Practice: Modeling a restaurant"""

    def __init__(self, name, cuisine_type):
        """Initialize name and cuisine type attributes"""
        """there are two attributes: name and cuisine_type"""
        self.name = name
        self.cuisine_type = cuisine_type

    """Two methods"""

    def describe_restaurant(self):
         """Simulate a rolling over in response to a command"""
         information = f"{self.name}, {self.cuisine_type}"
         return information

    def open_restaurant(self):
        """prints a msg that the rest. is open"""
        print(f"{self.name} is now open.")


my_restaurant = Resturant('El Milagro', 'Mexican')
print(f"My restaurant's name is {my_restaurant.name}")
print(f"My restaurant's cusine is {my_restaurant.cuisine_type}")
print(my_restaurant.describe_restaurant())
print(my_restaurant.open_restaurant())