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
import model as m
import csv
import time


def initCatalog():
    catalog = m.newCatalog()
    return catalog


def loadData(catalog):
    start_time = time.process_time()
    loadArtists(catalog)
    loadArtworks(catalog)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    print("Tiempo empleado: ",elapsed_time_mseg)


def loadArtists(catalog):
    artistsfile = cf.data_dir + 'MoMa/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        m.addArtist(catalog, artist)


def loadArtworks(catalog):
    artworksfile = cf.data_dir + 'MoMa/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in input_file:
        m.addArtwork(catalog, artwork)

def OrdenarArtists(catalog,anioInicial,anioFinal):
    return m.OrdenarArtistas(catalog,anioInicial,anioFinal)


def OrdenarArtworks(catalog, anioInicial, mesInicial, diaInicial, anioFinal, mesFinal, diaFinal):
    return m.OrdenarArtworks(catalog, anioInicial, mesInicial, diaInicial, anioFinal, mesFinal, diaFinal)


def artworksNacionalidad(catalog):
    return m.artworksNacionalidad(catalog)


def costoTransDept(catalog, dept):
    return m.transporteDepartamento(catalog, dept)