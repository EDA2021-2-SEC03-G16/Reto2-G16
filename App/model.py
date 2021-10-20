import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.ADT import map as map
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as merge
assert cf

# Construccion de modelos

def newCatalog():
    catalog = {'Artistas': None,
    'Obras': None,
    'TecnicaObras': None,
    'NacionalidadArtistas':None,
    'artistId':None}

    catalog['Artistas'] = map.newMap(34000,maptype='PROBING',loadfactor=0.5)
    
    catalog['Obras'] = map.newMap(294,maptype='PROBING',loadfactor=4.0)
    
    catalog['TecnicaObras'] = map.newMap(1200,maptype='CHAINING',loadfactor=0.80)
    
    catalog['NacionalidadArtistas'] = map.newMap(200,maptype='CHAINING',loadfactor=0.80)

    catalog['FechaArtista'] = map.newMap(1200,maptype='CHAINING',loadfactor=4.0,comparefunction=compareBirthArtist)

    catalog['artistID'] = map.newMap(17000,maptype='CHAINING',loadfactor=0.8,comparefunction=compareArtistsID)

    catalog['Fecha'] = map.newMap(40000,maptype='CHAINING',loadfactor=4.0,comparefunction=compareArtworksByAdDAte)

    catalog['Departmento'] = map.newMap(1200,maptype='CHAINING',loadfactor=4.0,comparefunction=compareArtworksByDepartment)

    catalog['Nacionalidad'] = map.newMap(500,maptype='CHAINING',loadfactor=4.0,comparefunction=compareCountryByNumberOfArtworks)

    return catalog

def ArtistsSize(catalog):
    return map.size(catalog['Artistas'])

def ArtworksSize(catalog):
    return map.size(catalog['Obras'])


def addArtist(catalog, Name, constituentid, Nationality, BeginDate, EndDate, Gender):
    if map.contains(catalog['artistID'], constituentid) is False:
        map.put(catalog['artistID'], constituentid, Name)
        artista = {}
        artista['Nationality']=Nationality
        artista['BeginDate']=BeginDate
        artista['EndDate']=EndDate
        artista['Gender']=Gender
        listaArtistaObra = lt.newList('ARRAY_LIST')
        artista['Artworks'] = listaArtistaObra
        map.put(catalog['Artistas'], Name, artista)
    if map.contains(catalog['Fecha'], BeginDate) is False:
        listaFehaArtista = lt.newList("ARRAY_LIST")
        diccionario = {}
        diccionario['Name']=Name
        diccionario['BeginDate']=BeginDate
        diccionario['Gender']=Gender
        diccionario['Nationality']=Nationality
        diccionario['EndDate']=EndDate
        lt.addLast(listaFehaArtista, diccionario)
        map.put(catalog['Fecha'], BeginDate, listaFehaArtista)
    else:
        diccionarioFechaArtista = {}
        entryFechaArtista=map.get(catalog['Fecha'], BeginDate)
        listaFechaArtista=me.getValue(entryFechaArtista)
        diccionarioFechaArtista['name']=Name
        diccionarioFechaArtista['Gender']=Gender
        diccionarioFechaArtista['Nationality']=Nationality
        diccionarioFechaArtista['BeginDate']=BeginDate
        diccionarioFechaArtista['EndDate']=EndDate
        lt.addLast(listaFechaArtista, diccionarioFechaArtista)


def addArtwork(catalog, title, DateAcquired, listamedium, Dimensions, listaconstituentid,
               ObjectID,CreditLine, Date, Classification, Height, Width, Department, Length, Weight):

    diccionarioObras = nuevaObra(title)
    diccionarioObras['ObjectID']=ObjectID
    diccionarioObras['ArtistsID']=listaconstituentid
    diccionarioObras['Medium']=listamedium
    diccionarioObras['Artists'] = listaconstituentid
    diccionarioObras['DateAcquired']=DateAcquired
    diccionarioObras['Dimensions']=Dimensions
    diccionarioObras['CreditLine']=CreditLine
    diccionarioObras['Date']=Date
    diccionarioObras['Department']=Department
    diccionarioObras['Classification']=Classification
    diccionarioObras['Height (cm)']=Height
    diccionarioObras['Width (cm)']=Width
    diccionarioObras['Length (cm)']=Length
    diccionarioObras['Weight (kg)']=Weight
    lt.addLast(catalog['Obras'], diccionarioObras)
    for i in listaconstituentid:
        lstArtworksCountry = lt.newList('ARRAY_LIST')
        if map.contains(catalog['artistID'], i):
            entryID=map.get(catalog['artistID'], i)
            name=me.getValue(entryID)
            entryNacionalidad = map.get(catalog['Artistas'], name)
            nationality = (me.getValue(entryNacionalidad))['Nationality']
            if map.contains(catalog['NacionalidadArtistas'], nationality) is False:
                obras = {}
                obras['Title'] = title
                obras['Date']=Date
                obras['Medium']=listamedium
                obras['Dimensions']=Dimensions
                obras['Artists']=listaconstituentid
                lt.addLast(lstArtworksCountry, obras)
                map.put(catalog['NacionalidadArtistas'], nationality, lstArtworksCountry)
            else:
                entry = map.get(catalog['NacionalidadArtistas'], nationality)
                lstArtworksCountry = me.getValue(entry)
                obras={}
                obras['Title']=title
                obras['Date']=Date
                obras['Medium']=listamedium
                obras['Dimensions']=Dimensions
                obras['Artists'] = listaconstituentid
                lt.addLast(lstArtworksCountry, obras)
        entryIDname = map.get(catalog['artistID'], i)
        IDname = me.getValue(entryIDname)
        entryLstArtworks = map.get(catalog['Artistas'], IDname)
        diccionarioArtista = me.getValue(entryLstArtworks)
        dictObra={}
        dictObra['Title']=title
        dictObra['Date']=Date
        dictObra['Medium']=listamedium
        dictObra['Dimensions']=Dimensions
        dictObra['DateAcquired']=DateAcquired
        dictObra['Department']=Department
        dictObra['Dimensions']=Dimensions
        dictObra['Classification']=Classification
        lt.addLast(diccionarioArtista['Artworks'], dictObra)
    if map.contains(catalog['Fecha'], DateAcquired) is False:
        listaFechas = lt.newList("ARRAY_LIST")
        fecha = {}
        fecha['Title'] = title
        fecha['Date']=Date
        fecha['Medium']=listamedium
        fecha['Dimensions']=Dimensions
        fecha['CreditLine']=CreditLine
        listaArtworkArtists = lt.newList('ARRAY_LIST')
        for i in listaconstituentid:
            entrycID = map.get(catalog['artistID'], i)
            nameArtist = me.getKey(entrycID)
            lt.addLast(listaArtworkArtists, nameArtist)
        fecha['Artists'] = listaArtworkArtists
        lt.addLast(listaFechas, fecha)
        map.put(catalog['Fecha'], DateAcquired, listaFechas)
    else:
        fecha={}
        entryadDate = map.get(catalog['Fecha'], DateAcquired)
        listaFecha = me.getValue(entryadDate)
        fecha['Title']=title
        fecha['Date']=Date
        fecha['Medium']=listamedium
        fecha['Dimensions']=Dimensions
        fecha['CreditLine']=CreditLine
        lstArtworkArtists = lt.newList('ARRAY_LIST')
        for i in listaconstituentid:
            entrycID = map.get(catalog['artistID'], i)
            nameArtist = me.getValue(entrycID)
            lt.addLast(lstArtworkArtists, nameArtist)
        fecha['Artists'] = lstArtworkArtists
        lt.addLast(listaFecha, fecha)
    if map.contains(catalog['Departmento'], Department) is False:
        listaDepartmento = lt.newList('ARRAY_LIST')
        departamento={}
        departamento['Title']=title
        departamento['Date']=Date
        departamento['Classification']=Classification
        departamento['Medium']=listamedium
        departamento['Dimensions']=Dimensions
        departamento['Weight (kg)']=Weight
        departamento['Length (cm)']=Length
        departamento['Height (cm)']=Height
        departamento['Width (cm)']=Width
        lt.addLast(listaDepartmento, departamento)
        map.put(catalog['Departmento'], Department, listaDepartmento)
    else:
        departamento={}
        entryDep = map.get(catalog['Departmento'], Department)
        listaDepartmento = me.getValue(entryDep)
        departamento['Title'] = title
        departamento['Date']=Date
        departamento['Classification']=Classification
        departamento['Medium']=listamedium
        departamento['Dimensions']=Dimensions
        departamento['Weight (kg)']=Weight
        departamento['Length (cm)']=Length
        departamento['Height (cm)']=Height
        departamento['Width (cm)']=Width
        listaArtworkArtists = lt.newList('ARRAY_LIST')
        for i in listaconstituentid:
            entrycID = map.get(catalog['artistID'], i)
            nameArtist = me.getValue(entrycID)
            lt.addLast(listaArtworkArtists, nameArtist)
        departamento['Artists'] = listaArtworkArtists
        lt.addLast(listaDepartmento, departamento)


def nuevaObra(title):
    nuevadiccionarioObra={'Title': "", 'DateAcquired': 0, 'ArtistsID': None, 'Medium': None,'Dimensions': "", 
                            'ObjectID': 0, "CreditLine": "", "Artists": [], 'Date': "",'Classification': "", 
                            'Height (cm)': 0, 'Width (cm)': 0, 'Department': "", 'Length (cm)': 0, 'Weight (kg)': 0}
    nuevadiccionarioObra['Title']=title
    return nuevadiccionarioObra


def sortArtists (catalog, anoinicial, anofinal):
    anokeys = map.keySet(catalog['FechaArtista'])
    listaAnos = lt.newList('ARRAY_LIST')
    for ano in lt.iterator(anokeys):
        if cmpArtistbyBirthDate(anoinicial, anofinal) is not False:
            if cmpArtistbyBirthDate(ano, anofinal) is not False:
                lt.addLast(listaAnos, ano)
    sub_list = listaAnos.copy()
    sorted_list = None
    sorted_list = merge.sort(sub_list,cmpArtistbyBirthDate)
    totalArtists = 0
    listaFinal=lt.newList('ARRAY_LIST')
    for i in lt.iterator(sorted_list):
        entryData = map.get(catalog['FechaArtista'],i)
        data = me.getValue(entryData)
        for j in lt.iterator(data):
            diccionario = {}
            diccionario['Nombre']=j['name']
            if j['BeginDate']=='0':
                diccionario['año nacimiento'] = 'No se tienen datos'
            else:
                diccionario['año nacimiento'] = j['BeginDate']
            if j['EndDate'] == '0':
                diccionario['año fallecimiento'] = ''
            else:
                diccionario['año fallecimiento'] = j['EndDate']
            diccionario['Nacionalidad'] = j['Nationality']
            diccionario['Género'] = j['Gender']
            lt.addLast(listaFinal,diccionario)
            totalArtists += 1
    return (listaFinal, totalArtists)

def sortArtworksByAdDate(catalog, d1, d2):
    dateLst = map.keySet(catalog['Fecha'])
    finalDateLst = lt.newList('ARRAY_LIST')
    for date in lt.iterator(dateLst):
        if cmpArtworkByDateAcquired(d1, date) is True:
            if cmpArtworkByDateAcquired(date, d2) is True:
                lt.addLast(finalDateLst, date)

    sub_list = finalDateLst.copy()
    sorted_list = None
    sorted_list = merge.sort(sub_list, cmpArtworkByDateAcquired)

    totalArtworks = 0
    totalPurchasedartworks = 0
    lstFinal = lt.newList('ARRAY_LIST')
    for element in lt.iterator(sorted_list):
        entryData = map.get(catalog['Fecha'], element)
        data = me.getValue(entryData)
        adDate = me.getKey(entryData)
        dicT = {}
        for lstElement in lt.iterator(data):
            dicT['Title'] = lstElement['Title']
            dicT['DateAcquired'] = adDate
            dicT['Date'] = lstElement['Date']
            dicT['Artists'] = lstElement['Artists']
            dicT['Medium'] = lstElement['Medium']
            dicT['Dimensions'] = lstElement['Dimensions']
            lt.addLast(lstFinal, dicT)
            totalArtworks += 1
            if 'Purchase' in lstElement['CreditLine']:
                totalPurchasedartworks += 1
    return lstFinal, totalArtworks, totalPurchasedartworks


def ObrasPorNacionalidad(catalog):
    paises = map.keySet(catalog['NacionalidadArtistas'])
    lista = lt.newList('ARRAY_LIST')
    for pais in lt.iterator(paises):
        if (len(pais) > 0 and (pais!= 'Nationality unknown')):
            entryPais = map.get(catalog['NacionalidadArtistas'], pais)
            lstCountry = me.getValue(entryPais)
            ObrasArtistas = lt.size(lstCountry)
            map.put(catalog['Nacionalidad'], ObrasArtistas, pais)
            lt.addLast(lista, ObrasArtistas)
    sorted_list = None
    sorted_list = merge.sort(lista, cmpCountriesbyArtworks)
    listaOrdenada=lt.newList('ARRAY_LIST')
    for number in lt.iterator(sorted_list):
        diccionario = {}
        entryNumber = map.get(catalog['Nacionalidad'], number)
        NumeroPais = me.getValue(entryNumber)
        diccionario[NumeroPais] = number
        lt.addLast(listaOrdenada, diccionario)
    topPaises = lt.getElement(listaOrdenada, 1)
    topPaisesLista = list(topPaises.keys())
    topCountry = topPaisesLista[0]
    listaVerificada=[]
    listaDatos = lt.newList('ARRAY_LIST')
    entryTopCountry = map.get(catalog['NacionalidadArtistas'], topCountry)
    lstArtworksTopCountry = me.getValue(entryTopCountry)
    for artwork in lt.iterator(lstArtworksTopCountry):
        datos={}
        listaArtistas = lt.newList('ARRAY_LIST')
        if artwork['Title'] not in listaVerificada:
            for artista in artwork['Artists']:
                nombreArtistaEntry = map.get(catalog['artistID'], artista)
                nombreArtista = me.getValue(nombreArtistaEntry)
                lt.addLast(listaArtistas, nombreArtista)
            datos['Title'] = artwork['Title']
            datos['Artists'] = listaArtistas
            datos['Date'] = artwork['Date']
            datos['Medium'] = artwork['Medium']
            datos['Dimensions'] = artwork['Dimensions']
            lt.addLast(listaDatos, datos)
    return listaOrdenada, listaDatos


def compareBirthArtist(keyname, birthdate):
    birthEntry = me.getKey(birthdate)
    if (keyname == birthEntry):
        return 0
    elif (keyname > birthEntry):
        return 1
    else:
        return -1


def compareArtistsID(keyname, cID):
    cIDEntry = me.getKey(cID)
    if (keyname == cIDEntry):
        return 0
    elif (keyname > cIDEntry):
        return 1
    else:
        return -1


def compareNationality(keyname, nationality):
    nationalityEntry = me.getKey(nationality)
    if (keyname == nationalityEntry):
        return 0
    elif (keyname > nationalityEntry):
        return 1
    else:
        return -1


def compareArtworksByAdDAte(keyname, adDate):
    dateEntry = me.getKey(adDate)
    if (keyname == dateEntry):
        return 0
    elif (keyname > dateEntry):
        return 1
    else:
        return -1


def compareArtworksByDepartment(keyname, department):
    depEntry = me.getKey(department)
    if (keyname == depEntry):
        return 0
    elif (keyname > depEntry):
        return 1
    else:
        return -1


def compareCountryByNumberOfArtworks(keyname, department):
    depEntry = me.getKey(department)
    if (keyname == depEntry):
        return 0
    elif (keyname > depEntry):
        return 1
    else:
        return -1



# Funciones de ordenamiento


def cmpArtworksByDate(artwork1, artwork2):

    r = None
    date1 = artwork1['Date']
    date2 = artwork2['Date']
    if date1 == '':
        date1 = 2021

    if date2 == '':
        date2 = 2021

    if int(date1) < int(date2):
        r = True
    else:
        r = False
    return r

def cmpCountriesbyArtworks(country1, country2):

    r = None
    if country1 > country2:
        r = True
    else:
        r = False

    return r

def cmpArtistbyBirthDate(date1, date2):
    r = None
    if (int(date1)) <= (int(date2)):
        r = True
    else:
        r = False
    return r

def cmpArtworkByDateAcquired(artwork1, artwork2):
    """ Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2
        Args:
            artwork1: informacion de la primera obra que incluye su valor 'DateAcquired' 
            artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired' 
    """
    date1 = artwork1.split("-")
    date2 = artwork2.split("-")
    r = None
    if (len(date1) < 2):
        date1 = [2021, 10, 20]
        artwork1 = '2021-10-02'
    if (len(date2)) < 2:
        date2 = [2021, 10, 20]
        artwork2 = '2021-10-02'
    
    if int(date1[0]) < int(date2[0]):
        r = True
    elif int(date1[0]) > int(date2[0]):
        r = False
    elif int(date1[1]) < int(date2[1]):
        r = True
    elif int(date1[1]) > int(date2[1]):
        r = False
    elif int(date1[2]) < int(date2[2]):
        r = True
    elif int(date1[2]) > int(date2[2]):
        r = False

    return r
