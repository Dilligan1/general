import calculator

if __name__ == '__main__':
    calc = calculator.Calculator()
    calc.add_car(
        calculator.Car('BMW', 30000, 7, 1200, 2500)
    )
    calc.add_car(
        calculator.ElectricCar('Tesla Model X', 300000, 5500, 150)
    )
    calc.add_car(
        calculator.Car('BMW', 30000, 7, 1200, 2500)
    )

    calc.print_cars()