class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текущая скорость у {self.name}:  {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость у городской машины {self.name}: {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} выше чем у городской машины'
        else:
            return f'Скорость {self.name} приемлемая'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочей машины {self.name}: {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} превышена'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейская машина'
        else:
            return f'{self.name} не полицейская машина'


ferrari = SportCar(100, 'Красная', 'Феррари', False)
mercedes = TownCar(30, 'Белый', 'Мерседес', False)
skoda = WorkCar(70, 'Бело-синяя', 'Шкода', True)
ford = PoliceCar(110, 'Серый', 'Форд', True)
print(skoda.turn_left())
print(f'{mercedes.turn_right()}, {ferrari.stop()}')
print(f'{skoda.go()} {skoda.show_speed()}')
print(f'{skoda.name}  {skoda.color}')
print(f'{ferrari.name} полицейская машина? {ferrari.is_police}')
print(f'{skoda.name} полицейская машина? {skoda.is_police}')
print(ferrari.show_speed())
print(mercedes.show_speed())
print(ford.police())
print(ford.show_speed())
