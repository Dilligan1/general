from calculator import add_two_numbers
from calculator import Car, Calculator, ElectricCar
import pytest
from apis import get_power_price, get_gas_price


@pytest.mark.parametrize(
    'a,b,result',
    [
        (10, 15, 25),
        (20, 20, 40),
        (30, 34, 64),
        (100, 100, 200)

    ]
)
def test_sum(a, b, result):
    res = add_two_numbers(a, b)
    assert res == result


def test_gas():
    result = get_gas_price()
    assert isinstance(result, int) or isinstance(result, int)


def test_power():
    result = get_power_price()
    assert isinstance(result, int) or isinstance(result, int)


class TestApi:
    @pytest.mark.parametrize('functions', [get_gas_price, get_power_price])
    def test_gas_power(self, functions):
        result = functions()
        assert isinstance(result, int) or isinstance(result, int)

    @pytest.mark.parametrize(
        'a,b,result',
        [
            (10, 15, 25),
            (20, 20, 40),
            (30, 34, 64),
            (100, 100, 200)

        ]
    )
    def test_sum(self, a, b, result):
        res = add_two_numbers(a, b)
        assert res == result


class TestCar:

    def test_static_year_cost(self, car):
        res = car.static_year_cost()
        assert res == 3700

    @pytest.mark.parametrize('miliage', [1000, 10000])
    def test_dynamic_year_cost(self, car, miliage):
        res = car.dynamic_year_cost(miliage)
        expected = car.fuel_economy * miliage / 100 * get_gas_price()
        assert res == expected

    @pytest.mark.parametrize('miliage', [1000, 10000])
    def test_year_cost(self, car, miliage):
        res = car.year_cost(miliage)
        expected = car.static_year_cost() + car.dynamic_year_cost(miliage)
        assert res == expected


class TestElectroCar:

    @pytest.mark.parametrize('miliage', [100, 10000])
    def test_dynamic_year_cost(self, electro_car, miliage):
        assert electro_car.dynamic_year_cost(
            miliage) == electro_car.power_consumption * miliage / 1000 * get_power_price()


class TestCalculator:

    def test_add_car(self, calculator, car):
        calculator.add_car(car)  # Добавляем автомобиль в калькулятор
        assert calculator.cars  # Проверяем, что список cars не пустой
        assert car in calculator.cars  # Проверяем, что автомобиль добавлен

    def test_print_cars(self, calculator):
        calculator.print_cars()

    def test_get_left_price(self, car, calculator):
        res = calculator.get_left_price()
        assert res
