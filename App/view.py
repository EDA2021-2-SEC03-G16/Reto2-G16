"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

import config as cf
import sys
import controller
from DISClib.ADT import map as mp
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
#MENU

def printMenu():
    print("*******************************************")
    print("    BIENVENIDO AL CATALOGO DE MoMA'S")
    print("*****       ********       *******    *****")
    print("")
    print("1. Cargar información del catálogo")
    print("2. Obras por Tecnica")
    print("0. Salir")
    print("")
    print("*******************************************")

#CARGA DE DATOS [1]
def initCatalog():
    return controller.initCatalog()

def loadData(catalog):
    controller.loadData(catalog)

catalog = None

#REQ1 [2]

def Tecnicas(catalog):
    no=int(input("Ingrese el numero de obras para consultar: "))
    tec=input("Ingrese la técnica para consultar: ")
    ret=controller.Tecnica(catalog,no,tec)
    return ret

#MENU PRINCIPAL

while True:
    printMenu()
    inputs = input('Escoja una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información ***") 
        catalog = initCatalog()
        loadData(catalog)
        print(" ")
        print('Artistas: ' + str(controller.ArtistsSize(catalog)))
        print(" ")
        print('Obras: ' + str(controller.ArtworksSize(catalog)))
        print(" ")

    elif int(inputs[0]) == 2:
        lista=Tecnicas(catalog)
        print(lista)

    else:
        sys.exit(0)
sys.exit(0)