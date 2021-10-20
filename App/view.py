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
import controller as c
from DISClib.ADT import map as map
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printResultados3(respuesta):
        print('En el rango seleccionado hay ' + str(respuesta[1]) + ' artistas.')
        print("****************************************************************")
        print('Los 3 primeros artistas del rango son: ')
        print(respuesta[0]['elements'][0])
        print(respuesta[0]['elements'][1])
        print(respuesta[0]['elements'][2])
        print("****************************************************************")
        print('Las ultimas 3 obras del rango son: ')
        print(respuesta[0]['elements'][-1])
        print(respuesta[0]['elements'][-2])
        print(respuesta[0]['elements'][-3])
        print("****************************************************************")

def printSortedResults(result):

    print('En el rango dado hay: ' + str(result[1]))
    print('De esas obras se compraron: '+ str(result[2]))
    print('Las primeras 3 obras del rango son: ')
    print(result[0]['elements'][0])
    print(result[0]['elements'][1])
    print(result[0]['elements'][2])
    print('Las ultimas 3 obras del rango en son: ')
    print(result[0]['elements'][-1])
    print(result[0]['elements'][-2])
    print(result[0]['elements'][-3])


def printObrasPorNacionalidad(respuesta):
    lista = lt.subList(respuesta[0], 1, 10)
    fechaInicio = [respuesta[1]['elements'][0], respuesta[1]['elements'][1], respuesta[1]['elements'][2], respuesta[1]['elements'][3], respuesta[1]['elements'][4]]
    fechaFin = [respuesta[1]['elements'][-1], respuesta[1]['elements'][-2], respuesta[1]['elements'][-3], respuesta[1]['elements'][-4], respuesta[1]['elements'][-5]]
    print('TOP 10 paises: ')
    print(lista['elements'])
    size = lt.size(respuesta[1])
    print('El número de obras son: ' + str(size))
    print('Las primeras 3 obras son: ')
    print(fechaInicio[0])
    print(fechaInicio[1])
    print(fechaInicio[2])
    print('Las últimas 3 obras son: ')
    print(fechaFin[0])
    print(fechaFin[1])
    print(fechaFin[2])

#MENU

def printMenu():
    print("*******************************************")
    print("    BIENVENIDO AL CATALOGO DE MoMA'S       ")
    print("*****       ********       *******    *****")
    print("")
    print("1. Cargar información del catálogo")
    print("2. Listar cronologicamente los artistas.")
    print("3. Listar cronologicamente las adquisiciones.")
    print("4. Clasificar las obras por técnica.")
    print("5. Clasificar las obras por la nacionalidad.")
    print("6. Transporte de obras por departamento.")
    print("0. Salir.")
    print("")
    print("*******************************************")

#CARGA DE DATOS [1]
def initCatalog():
    return c.initCatalog()

def loadData(catalog):
    c.loadData(catalog)

catalog = None

#REQ1 [2]


#MENU PRINCIPAL

while True:
    printMenu()
    inputs = input('Escoja una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información ***") 
        catalog = initCatalog()
        loadData(catalog)
        print(" ")
        print('Número de Artistas en el catálogo: ' + str(c.ArtistsSize(catalog)))
        print(" ")
        print('Número de Obras en el catálogo: ' + str(c.ArtworksSize(catalog)))
        print(" ")

    elif int(inputs[0]) == 2:
        anoainicial = int(input('Indique el año inicial:'))
        anofinal = int(input('Indique el año final:'))
        respuesta = c.sortArtists(catalog,anoainicial,anofinal)
        printResultados3(respuesta)

    elif int(inputs[0]) == 3:
        ainicial=input('Indique la fecha inicial de las obras que desea consultar (AAAA-MM-DD): ')
        afinal=input('Indique la fecha final de las obras que desea consultar (AAAA-MM-DD): ')
        result = c.sortArtworksByAdDate(catalog, ainicial, afinal)
        printSortedResults(result)
        print("****************************************************************")

    elif int(inputs[0]) == 4:
        pass

    elif int(inputs[0]) == 5:
        result = c.ObrasPorNacionalidad(catalog)
        printObrasPorNacionalidad(result)

    elif int(inputs[0]) == 6:
        pass
    else:
        sys.exit(0)
sys.exit(0)