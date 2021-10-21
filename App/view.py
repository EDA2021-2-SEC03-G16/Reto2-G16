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
import time
import sys
import controller as c
from DISClib.ADT import list as lt
assert cf

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


def initCatalog():
    return c.initCatalog()


def loadData(catalog):
    c.loadData(catalog)


def printArtistasCronologico(artistas):
    diccionario = lt.size(artistas)
    print("Número total de artistas en dicho rango: "+str(diccionario)+"\n")
    print("Los primeros y últimos 3 artistas son: ")
    for i in range(1,4):
        print("Nombre: "+lt.getElement(artistas,i)["DisplayName"])
        print("Año de nacimiento: "+lt.getElement(artistas,i)["BeginDate"])
        print("Año de fallecimiento: "+lt.getElement(artistas,i)["EndDate"])
        print("Nacionalidad: "+lt.getElement(artistas,i)["Nationality"])
        print("Género: "+lt.getElement(artistas,i)["Gender"])
    for i in range(-2,1):
        print("Nombre: "+lt.getElement(artistas,diccionario+i)["DisplayName"])
        print("Año de nacimiento: "+lt.getElement(artistas,diccionario+i)["BeginDate"])
        print("Año de fallecimiento: "+lt.getElement(artistas,diccionario+i)["EndDate"])
        print("Nacionalidad: "+lt.getElement(artistas,diccionario+i)["Nationality"])
        print("Género: "+lt.getElement(artistas,diccionario+i)["Gender"])
        

def printArtworksOrdenado(artworks):
    diccionario = lt.size(artworks[1])
    print("Número total de obras: "+str(diccionario)+"\n")
    print("Número total de obras adquiridas: "+str(artworks[0])+"\n")
    printArtworks(artworks,diccionario)


def printArtworks(artworks, numero):
    print("Sus primeras y últimas 3 obras son: \n")
    for i in range(1,4):
        print("Título: "+lt.getElement(artworks[1],i)["Title"])
        print("Artista: "+str(lt.getElement(artworks[1],i)["Artists"]["elements"])[1:-1])
        print("Tecnica: "+lt.getElement(artworks[1],i)["Medium"])
        print("Dimensiones: "+lt.getElement(artworks[1],i)["Dimensions"])
    for i in range(-2,1):
        print("Título: "+lt.getElement(artworks[1],numero+i)["Title"])
        print("Artista: "+str(lt.getElement(artworks[1],numero+i)["Artists"]["elements"])[1:-1])
        print("Tecnica: "+lt.getElement(artworks[1],numero+i)["Medium"])
        print("Dimensiones: "+lt.getElement(artworks[1],numero+i)["Dimensions"])
    

def printNacionalidadObras(respuesta):
    print("TOP 10 de las nacionalidades son:")
    for i in range(1,11): 
        print(lt.getElement(respuesta[0],i)[0]+" : "+str(lt.getElement(respuesta[0],i)[1]))
    print("La nacionalidad con más obras es: ",lt.getElement(respuesta[0],1)[0])
    lista = lt.size(respuesta[1])
    printArtworks(respuesta, lista)

def printTransportePorDepartamento(respuesta):
    print("Total de obras para transportar: ")
    print(respuesta[0])
    print("Precio estimado: ")
    print(respuesta[1])
    print("Las 5 obras más antiguas son: ")
    for i in range(1, lt.size(respuesta[3])+1):
        print("Título: "+lt.getElement(respuesta[3],i)[0]["Title"])
        print("Artista: "+str(lt.getElement(respuesta[3],i)[0]["Artists"]["elements"])[1:-1])
        print("Clasificación: "+lt.getElement(respuesta[3],i)[0]["Classification"])
        print("Tecnica: "+lt.getElement(respuesta[3],i)[0]["Medium"])
        print("Dimensiones: "+lt.getElement(respuesta[3],i)[0]["Dimensions"])
        print("Costo del transporte: "+str(round(lt.getElement(respuesta[3],i)[1],3)))
    print("\nLas 5 obras más costosas a transportar son: ")
    for i in range(1, lt.size(respuesta[4])+1):
        print("Título: "+lt.getElement(respuesta[4],i)[0]["Title"])
        print("Artista: "+str(lt.getElement(respuesta[4],i)[0]["Artists"]["elements"])[1:-1])
        print("Clasificación: "+lt.getElement(respuesta[4],i)[0]["Classification"])
        print("Tecnica: "+lt.getElement(respuesta[4],i)[0]["Medium"])
        print("Dimensiones: "+lt.getElement(respuesta[4],i)[0]["Dimensions"])
        print("Costo del transporte: "+str(round(lt.getElement(respuesta[4],i)[1],3)))
catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción: ')
    if int(inputs[0]) == 1:
        print("Cargando información ***")
        catalog = initCatalog()
        loadData(catalog)
        sizeArtists = int(lt.size(catalog['artists']))
        sizeArtworks = int(lt.size(catalog['artworks']))
        print('Número de artistas cargados en el catalogo: ' + str(sizeArtists))
        print('Número de obras cargadas en el catalogo: ' + str(sizeArtworks))
        print('Los tres últimos artistas son:')
        i=2
        while i>=0:
            diccionarioArtistas = lt.getElement(catalog['artists'],(sizeArtists-i))
            print(diccionarioArtistas)
            i-=1
        print('Las últimas tres obras son: ')
        i=2
        while i>=0:
            diccionarioArtworks = lt.getElement(catalog['artworks'],(sizeArtworks-i))
            print(diccionarioArtworks)
            i-=1

    
    elif int(inputs[0]) == 2:
        anioInicial = int(input("Ingrese el año incial del rango: "))
        anioFinal = int(input("Ingrese el año final del rango: "))
        start_time = time.process_time()
        printArtistasCronologico(c.OrdenarArtists(catalog,anioInicial,anioFinal))
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print("Tiempo empleado: ",elapsed_time_mseg)

    elif int(inputs[0]) == 3:
        diaInicial = int(input("Ingrese el día incial: "))
        mesInicial = int(input("Ingrese el mes incial: "))
        anioInicial = int(input("Ingrese el año incial: "))
        diaFinal = int(input("Ingrese el día final: "))
        mesFinal = int(input("Ingrese el mes final: "))
        anioFinal = int(input("Ingrese el año final: "))
        start_time = time.process_time()
        printArtworksOrdenado(c.OrdenarArtworks(catalog, anioInicial, mesInicial, diaInicial, anioFinal, mesFinal, diaFinal))
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print("Tiempo empleado: ",elapsed_time_mseg)

    elif int(inputs[0]) == 4:
        pass
        start_time = time.process_time()
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print("Tiempo empleado: ",elapsed_time_mseg)

    elif int(inputs[0]) == 5:
        start_time = time.process_time()
        result = c.artworksNacionalidad(catalog)
        printNacionalidadObras(result)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print("Tiempo empleado: ",elapsed_time_mseg)

    elif int(inputs[0]) == 6:
        departamento = input("Ingrese el departamento a consultar el costo de transporte: ")
        start_time = time.process_time()
        printTransportePorDepartamento(c.costoTransDept(catalog, departamento))
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print("Tiempo empleado: ",elapsed_time_mseg)

    else:
        sys.exit(0)
sys.exit(0)