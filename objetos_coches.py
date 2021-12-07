#es el modulo principal donde se van a importar los otros codigos

import persistencia_pickle as pp #se le cambia el nombre a pp para que sea mas corto
import car_class
import random as rd
FILE = 'Coches.obj.txt'

lista_coches = pp.retrieve(FILE)
if lista_coches == None:
    lista_coches = []
while True:
    marca = input('Dime la marca del coche: ')
    if marca == 'fin':
        break
    modelo = input('Dime el modelo del coche: ')
    combustible = input('Dime el combustible del coche: ')
    cilindrada = input('Dime la cilindrada del coche: ')
    ancho = input('Dime el ancho del coche: ')
    rodadura = input('Dime la rodadura del coche: ')
    diametro = input('Dime el diametro de la rueda del coche: ')
    presion = input('Dime la presión de las ruedas del coche: ')

    wheel = car_class.Wheel(ancho, rodadura, diametro)
    wheel.set_pressure(presion)
    coche = car_class.Car(marca, modelo,combustible, cilindrada)
    coche.set_wheel(wheel)

    lista_coches.append(coche) #se añade el objeto coche a la lista
    coche.move_pos(rd.random() *100, rd.random() *600) #como da valores entre 0 y 1 se multiplica por 100. Lo primero es la x lo segundo la y
    print('Posición: ', coche.get_pos())
    coche.move_incr(rd.random()*10, rd.random()*60)
    print('Posición: ', coche.get_pos())
    del (coche) #sirve para borrar lo que hay dentro de la lista

pp.store(lista_coches, FILE)
lista_coches = []
lista_coches = pp.retrieve(FILE)

for car in lista_coches: #hacemos el bucle para imprimir por pantalla uno a uno
    print('Marca, modelo, combustible, cilindrada: ', car.marca, car.modelo, car.combustible, car.cilindrada)
    print('Posición: ', car.get_pos(),'\n')
    print('Rueda: ', car.wheel.print_info(), 'Presión: ', car.wheel.presion)





