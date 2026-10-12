"""Act1. Create a class named Car with the following attributes: brand, model and color.
Add a method called show_info() that the full information of the car.
Then, create two objects of the Car class with different value and call the method to display their"""
class car: # Here we are creating a class called Car
    def __init__(self, brand, model, color): # This is the constructor: It is used to initialize the class's attributes. The problem asks for brand, model, and color because every car needs these attributes.
        # The self is how Python knows that this data belongs to that specific car and not to all cars.
        self.brand = brand # This is where the car's brand is stored
        self.model = model # This is where the car's model is stored
        self.color = color # This is where the car's color is stored

    def show_info(self): # This function displays the car information
        print(f"Brand: {self.brand}, Model: {self.model}, Color: {self.color}") # This line prints the car's brand, model, color
        # The f allows {self.attribute} to display the actual value in the text
        # We use {self.attribute} to display the data saved in the car

car1 = car("Chevrolet", "Suburban", "Blanco") # This is where we create a car (object) called car1. In my case, I entered Chevrolet as the brand, Suburban as the model, and White as the color, but you can customize this however you like.
car2 = car("Toyota", "Tacoma", "Azul") # And since the exercise asked us to create two objects, I created another one called car2, with the make Toyota, the model Tacoma, and the color Blue.

car1.show_info() # In this line, we ask the first car to display its information.
car2.show_info() # In this line, we ask the second car to display its information.