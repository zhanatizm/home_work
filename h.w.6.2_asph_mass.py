class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width


class MassCount(Road):
    def __init__(self, _length, _width, weightpersq, thickness):
        super().__init__(_length, _width)
        self.weight_per_sq = weightpersq
        self.thickness = thickness

    def mass(self):
        return (self._length * self._width * self.weight_per_sq * self.thickness) / 1000


r = MassCount(20, 5000, 25, 5)
print(f'Масса асфальта необходимая для покрытия дороги: {r.mass()} тонн')
