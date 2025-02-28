import pytest
from


@pytest.fixture()
def calculator(car):
    res = Calculator()
    res.add_car(car)
    return res



@pytest.fixture()
def car():
    print('\nСоздание нового автомобиля\n')
    return Car('BMW', 30000, 7, 1200, 2500)


@pytest.fixture()
def electro_car():
    return ElectricCar('BMW', 30000, 7, 1200)

