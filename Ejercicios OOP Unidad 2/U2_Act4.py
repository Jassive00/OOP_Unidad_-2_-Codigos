"""Act 4. Create a class Engine with a method start() that prints "Engine started".
Create a class Car that has an attribute engine (type Engine) and a method start_car() that calls
engine_start()."""
class Motor: # We create a class called Motor.
    def arrancar(self): # This is a method that involves starting the engine.
        print("Motor encendido") # Displays a message indicating that the engine is running.

class Auto: # We create a class called Auto.
    def __init__(self, motor): # The constructor receives a motor object.
        self.motor = motor # We kept that engine as part of the car.

    def arrancar_auto(self): # This method is for starting the car.
        self.motor.arrancar() # The car starts by calling the start() method of its engine.
"""This block defines the Car class.
In the constructor (__init__), it receives an object of type Engine and stores it as an attribute.
The start_car() method does not start the car directly; instead, it uses the engine to do so.
This demonstrates composition: a car has an engine and depends on it to function."""

motor = Motor() # We create an object of the Engine class.
auto1 = Auto(motor) # We create an object of the Car class that contains that engine.
auto1.arrancar_auto() # The car starts, but it actually calls the start() method of the engine.
