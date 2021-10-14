import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.ADT import map as map
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

# Construccion de modelos

def newCatalog():
    catalog = {'Artistas': None,'Obras': None,'Tecnica Obras': None}
    catalog['Artistas'] = map.newMap(76,maptype='PROBING',loadfactor=4.0)
    catalog['Obras'] = map.newMap(294,maptype='PROBING',loadfactor=4.0)
    catalog['Tecnica Obras'] = map.newMap(maptype='CHAINING',loadfactor=0.80)
    catalog["Nacionalidad Artistas"] = map.newMap(maptype='CHAINING',loadfactor=0.80)
    return catalog

def nationality (obras,artwork):

    nacionality=map.contains(obras, artwork["Nationality"])

    if nacionality:
        if artwork["Nationality"]!="":
            nacionalidad=map.get(obras,artwork["Nationality"])
            nacionalidad=me.getValue(nacionalidad)
            lt.addLast(nacionalidad,artwork)
        
    else:
        list=lt.newList("ARRAY_LIST")
        lt.addLast(list,artwork)
        map.put(obras, artwork["Nationality"],list)

def medium (obras,artwork):

    technic=map.contains(obras, artwork["Medium"])

    if technic:
        if artwork["Medium"]!="":
            tecnica=map.get(obras,artwork["Medium"])
            tecnica=me.getValue(tecnica)
            lt.addLast(tecnica,artwork)
        
    else:
        list=lt.newList("ARRAY_LIST")
        lt.addLast(list,artwork)
        map.put(obras, artwork["Medium"],list)
#  Informacion del catalogo

def addArtist(catalog, artist):

    artistas=catalog["Nacionalidad Artistas"]
    map.put(catalog['Artistas'], int(artist["ConstituentID"]), artist)
    nationality(artistas,artist)

def addArtwork (catalog, artwork):

    obras=catalog['Tecnica Obras']
    map.put(catalog['Obras'], int(artwork["ObjectID"]), artwork)
    medium(obras,artwork)



def Tecnica(catalogo,no,tec):
    print(tec+" ")
    tecnica = map.get(catalogo["Tecnica Obras"], tec)
    obra = lt.newList("ARRAY_LIST")
    print(tecnica+" ")
    if tecnica:
        lt.addLast(obra, me.getValue(tecnica))

        
    return obra

def ArtistsSize(catalog):
    return map.size(catalog['Artistas'])

def ArtworksSize(catalog):
    return map.size(catalog['Obras'])

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento