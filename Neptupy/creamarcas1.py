#!/usr/bin/env python3
from astropy.io import fits
import numpy as np
import os
from marcas_salida import exporta_reg
from photutils import daofind
from astropy.stats import mad_std
from photutils import aperture_photometry, CircularAperture

'''
Crea los archivos .reg para detección simple de fuentes sin tratamiento extra
para los ficheros CALIB en todos los directorios de imágenes en formato FITS de
VYGR2 de Neptuno con 4sigma!
'''

def nombre_sin_ext(ruta_fichero):
    '''
    Devuelve el nombre del archivo sin la extensión y con ella de la ruta de un
    fichero dado.
    '''
    sinext = (ruta_fichero.split('/'))[-1].split('.')[-2]
    conext = (ruta_fichero.split('/'))[-1]
    return (sinext, conext)

def soloruta(entrada):
    '''
    Devuelve solo la ruta donde un archivo entrada se encuentra
    '''
    entrada = entrada.split('/')[0:-1]
    carpeta = ''
    for palabra in entrada:
        carpeta = carpeta + palabra + '/'
    return carpeta

registro_log = ''
ruta1 = '../VGISS_FITS/'
rutas1 = os.listdir(ruta1)
rutasFITS = []
for ruta in rutas1:
    directorio = ruta1 + ruta + '/'
    #Lista de archivos total:
    archivos = os.listdir(directorio)
    #Agregar solo los CALIB:
    for archivo in archivos:
        if ('GEOMED' in archivo) and ('.fits' in archivo):
            rutasFITS.append(directorio + archivo)
conteo_arch = 0
cantidaddefits = len(rutasFITS)
#Ahora por cada archivo vamos a buscar y guardar!
for actual in rutasFITS:
    conteo_arch = conteo_arch + 1
    try:
        archivo_fits = fits.open(actual)
        data = archivo_fits[0].data
        data2 = data - np.median(data)
        # Next 2 lines determine search quality
        bkg_sigma = mad_std(data2)
        sources = daofind(data2, fwhm=4., threshold=5.*bkg_sigma)
        nombresalidareg = soloruta(actual) + nombre_sin_ext(actual)[0] + '_5.reg'
        aguardar = exporta_reg(nombresalidareg)
        contador = 0
        for punto in sources:
            contador = contador + 1
            xcord = punto['xcentroid'] + 1.0
            ycord = punto['ycentroid'] + 1.0
            aguardar.agrega_circulo(xcenter = xcord, ycenter = ycord, radius=5, texto='S' + str(contador))
        aguardar.escribe_reg()
        texto = 'Van ' + str(conteo_arch) + ' de ' + str(cantidaddefits) + '\n'
        print(texto, end='')
    except:
        texto = 'PROBLEMA EN' + actual
        print(texto, end='')
registro_log = registro_log + texto
g = open('log_out.txt', 'wb')
g.write(registro_log.encode('utf-8'))
g.close()
