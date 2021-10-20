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
 """

import config as cf
import time
import model as m
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo 

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = m.newCatalog()
    return catalog

# Carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    artist=loadArtists(catalog)
    artworks=loadArtworks(catalog)
    print("("+str(artist+artworks)+")")
    print("Técnica"+str(artworks))
    print("Nacionalidad"+str(artist))
    
    
def loadArtists(catalog):
    start_time = time.process_time() 
    booksfile = cf.data_dir + 'MoMA/Artists-utf8-large.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for artista in input_file:
        m.addArtist(catalog, artista['DisplayName'], artista['ConstituentID'],
                            artista['Nationality'], artista['BeginDate'], artista['EndDate'], artista['Gender'])
    stop_time = time.process_time() 
    elapsed_time_mseg = (stop_time - start_time)*1000  
    return elapsed_time_mseg     


def loadArtworks(catalog):
    start_time = time.process_time() 
    tagsfile = cf.data_dir + 'MoMA/Artworks-utf8-large.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for artwork in input_file:
        lstid = (artwork['ConstituentID'][1:-1]).split(", ")
        lstmedium = artwork['Medium'].split(",")
        m.addArtwork(catalog, artwork['Title'], artwork['DateAcquired'], lstmedium,
                         artwork['Dimensions'], lstid, artwork['ObjectID'], artwork['CreditLine'], artwork['Date'],
                         artwork['Classification'],artwork['Height (cm)'], artwork['Width (cm)'], artwork['Department'], 
                         artwork['Length (cm)'], artwork['Weight (kg)'])
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg
        

# Funciones de consulta sobre el catálogo

def ArtistsSize(catalog):
    return m.ArtistsSize(catalog)


def ArtworksSize(catalog):
    return m.ArtworksSize(catalog)


def sortArtists(catalog,year1,year2):
    return m.sortArtists(catalog,year1,year2)


def sortArtworksByAdDate(catalog, d1, d2):
    return m.sortArtworksByAdDate(catalog, d1, d2)


def classifyArtists(catalog,name):
    return m.classifyArtists(catalog,name)


def ObrasPorNacionalidad(catalog):
    return m.ObrasPorNacionalidad(catalog)
