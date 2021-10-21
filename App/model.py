"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import datetime as dat
import math
from DISClib.ADT import list as lt
from DISClib.ADT import map as map
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as merge
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de artistas. Crea una lista vacia para guardar
    todos los artistas, adicionalmente, crea una lista vacia para las obras. 
    Retorna el catalogo inicializado.
    """
    catalog = {'artists': None,
               'artworks': None,
               'date': None,
               'dateAdquirido': None,
               'medium': None,
               'nationality': None,
               'artistaObra': None}
    
    catalog['artists'] = lt.newList("SINGLED_LINKED", compareArtistsConstituentID)
    
    catalog['artworks'] = lt.newList("SINGLE_LINKED", compareArtworksID)
    
    catalog['fecha'] = map.newMap(150,maptype='CHAINING',loadfactor=4.0,comparefunction=compareArtistsFechaInicial)

    catalog['dateAdquirido'] = map.newMap(900,maptype='PROBING',loadfactor=0.5,comparefunction=compareArtworksFecha)

    catalog['tecnica'] = map.newMap(800,maptype='PROBING',loadfactor=0.5,comparefunction=compararArtworksTecnica)

    catalog['nacionalidad'] = map.newMap(100,maptype='CHAINING',loadfactor=4.0,comparefunction=compareArtworksNacionalidad)

    catalog['departamento'] = map.newMap(10,maptype='CHAINING',loadfactor=4.0,comparefunction=compareArtworksByArtist)

    catalog['artistaObra'] = map.newMap(2000, maptype='PROBING', loadfactor=0.5,comparefunction=compareArtworksByArtist)
    
    return catalog


def addArtist(catalog, artist):
    lt.addLast(catalog['artists'], artist)
    addFechaInicio(catalog, artist["BeginDate"], artist)


def addArtwork(catalog, artwork):
    nombres = encontrarNombresyNacionalidades(artwork["ConstituentID"][1:-1].split(","), catalog)
    artwork["Artists"] = nombres[0]
    artwork["Nationalities"] = nombres[1]
    lt.addLast(catalog['artworks'], artwork)
    addTecnica(catalog, artwork["Medium"], artwork)
    addAdquirido(catalog, artwork["DateAcquired"], artwork)
    addDepartmento(catalog, artwork["Department"], artwork)
    for nacion in lt.iterator(artwork["Nationalities"]):
        addNacionalidad(catalog, nacion, artwork)
    for artista in lt.iterator(artwork["Artists"]):
        addArtistaObra(catalog, artista, artwork)


def addFechaInicio(catalog, nameDate, artist):
    fechas = catalog['fecha']
    existDate = map.contains(fechas, str(nameDate))
    if existDate:
        entry = map.get(fechas, str(nameDate))
        date = me.getValue(entry)
    else:
        date = nuevaFecha(str(nameDate))
        map.put(fechas, str(nameDate), date)
    lt.addLast(date['artists'], artist)


def addAdquirido(catalog, nameDate, artwork):
    fechas = catalog['dateAdquirido']
    existDate = map.contains(fechas, str(nameDate))
    if existDate:
        entry = map.get(fechas, str(nameDate))
        date = me.getValue(entry)
    else:
        date = nuevoAdquirido(str(nameDate))
        map.put(fechas, str(nameDate), date)
    lt.addLast(date['artworks'], artwork)



def addTecnica(catalog, namemedium, artwork):
    tecnicas = catalog['tecnica']
    existmedium = map.contains(tecnicas, namemedium)
    if existmedium:
        entry = map.get(tecnicas, namemedium)
        medium = me.getValue(entry)
    else:
        medium = nuevaTecnica(namemedium)
        map.put(tecnicas, namemedium, medium)
    lt.addLast(medium['artworks'], artwork)


def addNacionalidad(catalog, nameNationality, artwork):
    nationalities = catalog['nacionalidad']
    if nameNationality == "":
        nameNationality = "Nationality unknown"
    existNationality = map.contains(nationalities, nameNationality)
    if existNationality:
        entry = map.get(nationalities, nameNationality)
        nationality = me.getValue(entry)
    else:
        nationality = nuevaNacionalidad(nameNationality)
        map.put(nationalities, nameNationality, nationality)
    lt.addLast(nationality['artworks'], artwork)


def addDepartmento(catalog, nameDepartment, artwork):
    departments = catalog['departamento']
    existDepartment = map.contains(departments, nameDepartment)
    if existDepartment:
        entry = map.get(departments, nameDepartment)
        department = me.getValue(entry)
    else:
        department = nuevoDepartamento(nameDepartment)
        map.put(departments, nameDepartment, department)
    lt.addLast(department['artworks'], artwork)


def addArtistaObra(catalog, nameArtist, artwork):
    artistas = catalog['artistaObra']
    existArtist = map.contains(artistas, nameArtist)
    if existArtist:
        entry = map.get(artistas, nameArtist)
        artist = me.getValue(entry)
    else:
        artist = nuevoArtistaObra(nameArtist)
        map.put(artistas, nameArtist, artist)
    lt.addLast(artist['artworks'], artwork)


def addMediumBono(medio, namemedium, artwork):
    existmedium = map.contains(medio, namemedium)
    if existmedium:
        entry = map.get(medio, namemedium)
        medium = me.getValue(entry)
    else:
        medium = nuevaTecnica(namemedium)
        map.put(medio, namemedium, medium)
    lt.addLast(medium['artworks'], artwork)


def nuevaFecha(nameDate):
    date = {'name': "",
            "artists": None}
    date['name'] = nameDate
    date['artists'] = lt.newList('SINGLE_LINKED', compareArtistsFechaInicial)
    return date


def nuevoAdquirido(nameDate):
    date = {'name': "","artworks": None}
    date['name'] = nameDate
    date['artworks'] = lt.newList('SINGLE_LINKED', compareArtworksFecha)
    return date


def nuevaTecnica(name):
    medium = {'name': "","artworks": None}
    medium['name'] = name
    medium['artworks'] = lt.newList('SINGLE_LINKED', compararArtworksTecnica)
    return medium


def nuevaNacionalidad(name):
    nationality = {'name': "","artworks": None}
    nationality['name'] = name
    nationality['artworks'] = lt.newList('SINGLE_LINKED', compareArtworksNacionalidad)
    return nationality


def nuevoDepartamento(name):
    department = {'name': "","artworks": None}
    department['name'] = name
    department['artworks'] = lt.newList('SINGLE_LINKED', compareArtworksNacionalidad)
    return department


def nuevoArtistaObra(name):
    artistaObra = {'name': "","artworks": None}
    artistaObra['name'] = name
    artistaObra['artworks'] = lt.newList('SINGLE_LINKED', compareArtworksNacionalidad)
    return artistaObra


def encontrarNombresyNacionalidades(artistas, catalog):
    nombres = lt.newList(datastructure="ARRAY_LIST")
    nacionalidades = lt.newList(datastructure="ARRAY_LIST")
    for id in artistas:
        encontro = False
        i = 0
        while not encontro and i< lt.size(catalog["artists"]):
            if lt.getElement(catalog["artists"],i)["ConstituentID"] == str(id).strip():
                lt.addLast(nombres, lt.getElement(catalog["artists"],i)["DisplayName"])
                lt.addLast(nacionalidades, lt.getElement(catalog["artists"],i)["Nationality"])
                encontro = True
            i += 1
    return nombres, nacionalidades


def getArtworksByMedium(catalog, namemedium):
    medium = map.get(catalog['tecnica'], namemedium)
    if medium:
        return me.getValue(medium)
    return None


def artworksNacionalidad(catalog):
    llaves = map.keySet(catalog["nacionalidad"])
    lstNacion = lt.newList(datastructure="ARRAY_LIST")
    for key in lt.iterator(llaves):
        tamanio = cantidadObrasPais(catalog, key)
        lt.addLast(lstNacion, (key,tamanio))
    ordenada = merge.sort(lstNacion, compararNacionalidad)
    nacionMayor = lt.getElement(ordenada,1)[0]
    nacion = map.get(catalog["nacionalidad"], nacionMayor)
    result = (me.getValue(nacion))["artworks"]
    return ordenada, result


def cantidadObrasPais(catalog, nacion):
    nacion = map.get(catalog["nacionalidad"], nacion)
    if nacion:
        result = (me.getValue(nacion))["artworks"]
        return lt.size(result)
    return None


def transporteDepartamento(catalog, departamento):
    costo=0
    peso=0
    total=0
    masCostosas=lt.newList(datastructure="ARRAY_LIST")
    masAntiguas=lt.newList(datastructure="ARRAY_LIST")
    completaCosto=not True
    completaAntiguedad=not True
    listaDepartamento=map.get(catalog["departamento"], departamento)
    if listaDepartamento:
        respuesta = (me.getValue(listaDepartamento))["artworks"]
        for artwork in lt.iterator(respuesta):
            if departamento==artwork["Department"]:
                precioObra = precioPorObra(artwork)
                costo+=precioObra[0]
                total+=1
                peso+=precioObra[1]
                if lt.size(masCostosas) < 5:
                    lt.addLast(masCostosas, [artwork,precioObra[0]])
                elif lt.size(masCostosas) == 5 and not completaCosto:
                    merge.sort(masCostosas, compararCosto)
                    completaCosto=not False
                else:
                    i=5
                    e1=not True
                    while i>0 and not e1:
                        if i==1:
                            lt.removeLast(masCostosas)
                            lt.insertElement(masCostosas,[artwork,precioObra[0]], i)
                            e1 = not False
                        elif precioObra[0] <= lt.getElement(masCostosas, i)[1]:
                            e1 = not False
                        elif precioObra[0] < lt.getElement(masCostosas, i-1)[1]:
                            lt.removeLast(masCostosas)
                            lt.insertElement(masCostosas, [artwork,precioObra[0]], i)
                            e1=not False
                        else:
                            i-=1
                if lt.size(masAntiguas)<5:
                    lt.addLast(masAntiguas, [artwork,precioObra[0]])
                elif lt.size(masAntiguas)==5 and not completaAntiguedad:
                    merge.sort(masAntiguas, compararArtworkDepartamento)
                    completaAntiguedad = not False
                else:
                    i=5
                    e2=not True
                    if artwork["Date"] != "":
                        while i>0 and not e2:
                            if i==1:
                                lt.removeLast(masAntiguas)
                                lt.insertElement(masAntiguas, [artwork,precioObra[0]], i)
                                e2=not False
                            elif artwork["Date"]>lt.getElement(masAntiguas, i)[0]["Date"]:
                                e2=not False
                            elif artwork["Date"]>lt.getElement(masAntiguas, i-1)[0]["Date"]:
                                lt.removeLast(masAntiguas)
                                lt.insertElement(masAntiguas, [artwork,precioObra[0]], i)
                                e2=not False
                            else:
                                i-=1
    costo=round(costo,2)
    peso=round(peso,2)
    return total, costo, peso, masAntiguas, masCostosas


def precioPorObra(artwork):
    peso=0
    precio=0
    l=0
    lado1=1
    lado2=1
    lado3=1
    lado4=1
    if (artwork["Weight (kg)"]!="") and (artwork["Weight (kg)"]!="0"):
        precio = 72*float(artwork["Weight (kg)"])
        peso += float(artwork["Weight (kg)"])
    if (artwork["Depth (cm)"]!="") and (artwork["Depth (cm)"]!="0"):
        lado1 = float(artwork["Depth (cm)"])/100
        l += 1
    if (artwork["Height (cm)"] !="") and (artwork["Height (cm)"]!="0"):
        lado2 = float(artwork["Height (cm)"])/100
        l += 1
    if (artwork["Length (cm)"]!="") and (artwork["Length (cm)"]!="0"):
        lado3 = float(artwork["Length (cm)"])/100
        l += 1
    if (artwork["Width (cm)"]!="") and (["Width (cm)"]!="0"):
        lado4 = float(artwork["Width (cm)"])/100
        l += 1
    if (artwork["Diameter (cm)"]!="") and (artwork["Diameter (cm)"]!="0") and (l<= 1):
        areaDiametro = (((((float(artwork["Diameter (cm)"])/2)**2)*math.pi)/10000)*lado1*lado2*lado3*lado4)
        if areaDiametro * 72 > precio:
            precio = areaDiametro*72
    if artwork["Circumference (cm)"] != "" and artwork["Circumference (cm)"] != "0" and l <= 1:
        areaCircunferencia = ((((float(artwork["Circumference (cm)"])**2)/(4*math.pi))/10000)*lado1*lado2*lado3*lado4)
        if areaCircunferencia * 72 > precio:
            precio = areaCircunferencia*72
    if l==2 or l==3:
        areaLado = (lado1*lado2*lado3*lado4)
        if areaLado * 72 > precio:
            precio = areaLado*72
    if precio == 0:
        precio = 48
    return precio, peso


def compareArtistsConstituentID(id1, id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def compareArtworksID(id1, id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def compareArtistsFechaInicial(date, fecha):
    llaveFecha = me.getKey(fecha)
    if (date == llaveFecha):
        return 0
    elif (date > llaveFecha):
        return 1
    else:
        return -1


def compareArtworksFecha(date1, fecha):
    llaveFecha=me.getKey(fecha)
    if (date1==llaveFecha):
        return 0
    elif (date1>llaveFecha):
        return 1
    else:
        return -1


def compararArtworksTecnica(medium, medio):
    llaveMedio = me.getKey(medio)
    if (medium == llaveMedio):
        return 0
    elif (medium > llaveMedio):
        return 1
    else:
        return -1


def compareArtworksNacionalidad(nationality, nacionalidad):
    llaveNacionalidad = me.getKey(nacionalidad)
    if (nationality == llaveNacionalidad):
        return 0
    elif (nationality > llaveNacionalidad):
        return 1
    else:
        return -1


def compararCosto(c1, c2):
    return c1[1] < c2[1]


def compareArtworksByArtist(artist, artista):
    llaveArtista = me.getKey(artista)
    if (artist == llaveArtista):
        return 0
    elif (artist > llaveArtista):
        return 1
    else:
        return -1
        

def compararNacionalidad(nacionalidad1, nacionalidad2):
    respuesta=nacionalidad1[1]>nacionalidad2[1]
    return respuesta


def comparaArtworAdquisicion(obra1, obra2):
    respuesta=(obra1)<(obra2) and obra1 != None and obra2 != None
    return respuesta

def compararObrasTecnica(t1, t2):
    if t1[0] == "":
        medio1 = (t1[0],0)
    if t2[0] == "":
        medio2 = (t2[0],0)
    return medio1[1]>medio2[1]


def compararArtworkDepartamento(obra1, obra2):
    respuesta=(str(obra1[0]["Date"])<str(obra2[0]["Date"])) and obra1[0]["Date"] != None and obra2[0]["Date"] != None
    return respuesta

def OrdenarArtistas(catalog,anioI,anioF):
    artistas = lt.newList(datastructure="ARRAY_LIST")
    for anio in range(anioI, anioF+1):
        date = map.get(catalog["fecha"], str(anio))
        if date:
            artistsDate = me.getValue(date)['artists']
            for artist in lt.iterator(artistsDate):
                lt.addLast(artistas, artist)
    return artistas


def OrdenarArtworks(catalog, anioInicial, mesInicial, diaInicial, anioFinal, mesFinal, diaFinal):
    obras=lt.newList(datastructure="ARRAY_LIST")
    fechaInicial=str(dat.datetime(anioInicial, mesInicial, diaInicial))
    fechaFinal=str(dat.datetime(anioFinal, mesFinal, diaFinal))
    llaves=map.keySet(catalog["dateAdquirido"])
    listaLlaves = lt.newList(datastructure="ARRAY_LIST")
    for llave in lt.iterator(llaves):
        if llave!=None and llave!="" and fechaInicial<=llave and fechaFinal>=llave:
            lt.addLast(listaLlaves, llave)
    llavesOrdenadas = merge.sort(listaLlaves, comparaArtworAdquisicion)
    adquiridas = 0
    for llave in lt.iterator(llavesOrdenadas):
        date = map.get(catalog["dateAdquirido"], str(llave))
        artworkDate = me.getValue(date)['artworks']
        for artwork in lt.iterator(artworkDate):
            lt.addLast(obras, artwork)
            if "purchase" in artwork["CreditLine"].lower():
                adquiridas += 1
    return adquiridas, obras