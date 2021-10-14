import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

# Construccion de modelos

def newCatalog():

    catalog = {'Artistas': None,
               'Obras': None,
               'Medios Obras': None}

    catalog['Artistas'] = mp.newMap(76,
                                   maptype='PROBING',
                                   loadfactor=4.0)

    catalog['Obras'] = mp.newMap(294,
                                   maptype='PROBING',
                                   loadfactor=4.0)

    catalog['Medios Obras'] = mp.newMap(maptype='CHAINING',loadfactor=0.80)

    catalog["Nacionalidad Artistas"] = mp.newMap(maptype='CHAINING',loadfactor=0.80)
    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    
    artistas=catalog["Nacionalidad Artistas"]
    mp.put(catalog['Artistas'], int(artist["ConstituentID"]), artist)
    add_map_bynationality(artistas,artist)

def addArtwork (catalog, artwork):

    obras=catalog['Medios Obras']

    mp.put(catalog['Obras'], int(artwork["ObjectID"]), artwork)
    add_map_bymedium(obras,artwork)

def add_map_bymedium (obras,artwork):

    b=mp.contains(obras, artwork["Medium"])

    if b:
        if artwork["Medium"]!="":
            a=mp.get(obras,artwork["Medium"])
            a=me.getValue(a)
            lt.addLast(a,artwork)
        
    else:
        lista=lt.newList("ARRAY_LIST")
        lt.addLast(lista,artwork)
        mp.put(obras, artwork["Medium"],lista)

def add_map_bynationality (obras,artwork):

    b=mp.contains(obras, artwork["Nationality"])

    if b:
        if artwork["Nationality"]!="":
            a=mp.get(obras,artwork["Nationality"])
            a=me.getValue(a)
            lt.addLast(a,artwork)
        
    else:
        lista=lt.newList("ARRAY_LIST")
        lt.addLast(lista,artwork)
        mp.put(obras, artwork["Nationality"],lista)


# Funciones para creacion de datos

# Funciones de consulta

def medioAntiguo(catalogo,num,medio):
    print(medio)#Exhibition catalogue with one loose editioned print
    medium = mp.get(catalogo["Medios Obras"], medio)
    oldartwork = lt.newList("ARRAY_LIST")
    print(medium)
    if medium:
        lt.addLast(oldartwork, me.getValue(medium))

        
    return oldartwork

def ArtistsSize(catalog):
    return mp.size(catalog['Artistas'])

def ArtworksSize(catalog):
    return mp.size(catalog['Obras'])

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento