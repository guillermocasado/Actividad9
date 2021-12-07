class Wheel:
    def __init__(self, ancho, rodadura, diametro):
        self.ancho = ancho
        self.rodadura = rodadura
        self.diametro = diametro
        self.presion = 0
        self.wheel = None
    def set_pressure(self, presion):
        self.presion = presion
    def print_info(self):
        print(f'{self.ancho}/{self.rodadura} R{self.diametro}')
class Car:
    def __init__(self, marca, modelo, combustible, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible
        self.cilindrada = cilindrada
        self.pos_x = 0
        self.pos_y = 0
    def move_pos(self, x, y):
        self.pos_x = x
        self.pos_y = y
    def move_incr(self, x, y):
        self.pos_x += x
        self.pos_y += y
    def get_pos(self):
        return self.pos_x, self.pos_y
    def set_wheel(self, wheel):
        self.wheel = wheel