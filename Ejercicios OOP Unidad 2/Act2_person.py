"""Act2. Create a class named Person with a constructor that recives the parameters name, age and city.
Add a method called greet() that display a message such as: "Hi, my name is Ana, I am 25 years old and I live in Mexico." 
Create three objects of the Person class and make each one call the greet() method."""
class Person: # We create a class called Person.
    def __init__(self, name, age, city): # The constructor: runs when we create a new Person. It asks for name, age and city because every person has this.
        # Self refers to this particular person.
        self.name = name # Here we store the name for this person.
        self.age = age # Here we store the age for this person.
        self.city = city # Here we store the city for this person.

    def greet(self): # This method is used to display a greeting along with the person's information.
        # Self inside the parentheses receives the current instance so that its data can be used.
        print(f"Hi, my name is {self.name}, I am {self.age} years old, and I live in {self.city}.")
        # We use f-strings (f“...”) to interpolate text with variables.
        # Whatever is inside { } is replaced with the actual value of each attribute.
        # self.name is this person's name, self.age is their age, and self.city is their city.

# We created three objects (people) with different data.
person1 = Person("Juan", 15, "Guadalajara") # We create an object called person1 with a name, age, and city.
person2 = Person("Maria", 22, "Tijuana") # We create an object called person2 with a name, age, and city
person3 = Person("Mateo", 18, "Culiacan") # We create an object called person3 with a name, age, and city
# The arguments enclosed in parentheses, such as (“Juan”, 15, “Guadalajara”), are the arguments passed to the __init__ constructor.
# “Juan” is stored in self.name.
# 15 is stored in self.age.
# “Guadalajara” is stored in self.city.

# We ask each person to show their greeting
person1.greet() # We call Juan's greet method, which uses its own data to print its message.
person2.greet() # We call Maria's greet method, which uses its own data to print its message
person3.greet() # We call Mateo's greet method, which uses its own data to print its message