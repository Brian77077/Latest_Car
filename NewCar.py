#!/usr/bin/python
# -*- coding: utf-8 -*-

# --------------------------------------------------------------------
# By: Brian Salinas
#     https://github.com/Brian77077/Latest_Car
# Purpose: Python 3.x code testbed, NOT compatible with Python 2.x.
# Initial Release Date: May 9, 2019
# --------------------------------------------------------------------

import car_controller


class Car:

    # Set initial variables for object Car.  It is important to call init & self this way, so that speed
    # and any other object properties remain persistent in memory, otherwise the values will be lost
    # when the method goes out of scope.
    def __init__(self, speed=0):
        # this init & self callouts will pass the following declarations to each instance of class Car.
        self.speed = speed
        self.odometer = 0
        self.time = 0
        self.counta = 0

    def say_state(self):
        print("I'm going {} kph!".format(self.speed))
        # This next line was added so i could see if the time was real time or a counter.
        print("time elapsed so far is {} hr, it's just using a counter".format(self.time))
        print(" ")

    def accelerate(self):
        self.speed += 5
        self.counta += 1        # This counter will let the user know how many times they
                                # hit the accelerator.

    def brake(self):
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5

    def step(self):
        self.odometer += self.speed
        #     Add two hrs to the time with every step vs. 1 hr.
        self.time += 2
        print("two hrs added to time counter.")

    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            pass

    def check_speeding(self):
        print(car_controller.status())  # Should print status message.
        if self.speed < 15:
            print("Not speeding")
        else:
            print("Slow down!)")
            print("You have hit the accelerator {} tmes".format(self.counta))


if __name__ == '__main__':

    # Now show if this file is the main or is imported.
    print("Car.py is being run directly, it is not being imported.")

    # My_car is an instance of the Car() Class.
    my_car = Car()
    print("I'm a car!")
    while True:
        action = input("What should I do? [A]ccelerate, [B]rake, "
                       "show [O]dometer, or show average [S]peed?").upper()
        if action not in "ABOST" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("The car has driven {} kilometers".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} kph".format(my_car.average_speed()))
        elif action == 'T':
            print("I added this text")

        my_car.step()
        my_car.say_state()
        my_car.check_speeding()
