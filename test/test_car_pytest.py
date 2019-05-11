import ssl
import pytest
from NewCar import Car

test_car = Car()
@pytest.fixture
def test_speeding():
    print("test speed check is called")
    test_car.speed = 50

def test_car_accelerate(test_car):
    test_car.accelerate()
    print("The current speed after accelerating is {} kph".format(test_car.speed))