#!/usr/bin/env python3
import numpy as np
from astropy.io import fits
from marcas_salida import exporta_reg

def buscaNeptuno(data_array):
    #Por escribir
    pass

def buscaEstrellas(data_array):
    #Por escribir
    pass

def buscaCuerpos(data_array):
    #Por escribir
    pass

def buscaNubes(data_array, coord_nept):
    #Por escribir
    pass

class imagen:
    '''
    Clase que determinará los objetos caracterizados por ser imágenes
    de Neptuno desde la sonda Voyager 2/NASA
    '''
    def __init__(self, rutaFITS):
        '''
        rutaFITS = Ruta del archivo .fits que contiene la imagen
        '''
        self.rutaFITS = rutaFITS
        archivo_f = fits.open(rutaFITS)
        #self.FITS_file = archivo_f[0]
        self.target = (archivo_f[0].header.get('6').split('"'))[1].split('"')[0]
        self.filtro = (archivo_f[0].header.get('15').split('"'))[1].split('"')[0]
        self.expo_time = float((archivo_f[0].header.get('17')).strip(' <SECOND>'))
        self.FITS_data = archivo_f[0].data
        self.dmax = np.max(self.FITS_data)
        self.dmin = np.min(self.FITS_data)
