# -*- coding: utf-8 -*-

from operaciones.suma import sumar
from operaciones.resta import restar
from operaciones.multiplicacion import multiplicar
from operaciones.division import dividir

if __name__ == "__main__":
    x = int(input("Ingresa el primer numero: "))
    y = int(input("Ingresa el segundo numero: "))

    print("Suma:", sumar(x, y))
    print("Resta:", restar(x, y))
    print("Multiplicacion:", multiplicar(x, y))
    print("Division:", dividir(x, y))

