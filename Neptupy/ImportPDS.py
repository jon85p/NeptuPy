#!/usr/bin/env python3

import os
from subprocess import check_call
from time import sleep
from astropy.io import fits
import warnings
warnings.filterwarnings("ignore")

def pds2fits(pdsFile, fitsFile, debug = False, ignore_existence = True):
    '''
    Converts a pdsFile .PDS from VYG2 to .FITS file
    Returns true or false from conversion status.

    Using ISIS3 from USGS
    {Integrated System for Imagers and Spectrometers (ISIS)}

    Parameters:
        pdsFile = String with the .LBL filename to convert
        fitsFile = String with the output filename
        debug = Boolean, debug mode
        ignore_existence = Ignore existence of output files

    '''

    #ISIS Root folder
    try:
      ISIS_ROOT = os.environ["ISISROOT"]
    except:
      print("The ISISROOT environment variable must be added, read the INSTALL file")
      exit(1)
    pds2isis = ISIS_ROOT + 'bin/pds2isis'
    isis2fits = ISIS_ROOT + 'bin/isis2fits'
    if ignore_existence == False:
        if os.path.isfile(fitsFile):
            #Existe el archivo fits, salir!
            return 1
    #Comprobación de existencia y permisos de lectura de los archivos de entrada
    if not os.path.isfile(pdsFile):
        raise NameError("The input file doesn't exist, exit! ", pdsFile)
    if not os.access(pdsFile, os.R_OK):
        raise NameError('The access to the file doesnt exist! ', pdsFile)
    #Primera conversión, de .img a partir del lbl a .cub
    cubfile = (fitsFile.split('/'))[-1].split('.')[-2]
    if debug:
        print('Start .cub conversion')
    check_call([pds2isis, 'FROM=' + pdsFile , 'TO=' + cubfile])
    if debug:
        print('Finish the cub conversion')
    #Acá debería ya estar guardado el archivo .cub
    cubfile = cubfile + '.cub'
    if debug:
        print('Start .fits conversion')
    check_call([isis2fits, 'FROM=' + cubfile , 'TO=' + fitsFile])
    if debug:
        print('Finish the .fits conversion')
    #Proceder a borrar los archivos .cub
    if debug:
        print('Deleting the .cub file')
    os.remove(cubfile)
    #Ahora viene la actualización de los headers del .fits con los datos en el
    #fichero .LBL)
    if debug:
        print('Start the headings adding')
    f = open(pdsFile, 'rb')
    texto = f.read().decode('utf8').split('\r\n')
    cont = -1
    for line in texto:
        cont = cont + 1
        if 'INSTRUMENT_HOST_NAME' in line:
            comienzo = cont
        if 'SPACECRAFT_CLOCK_STOP_COUNT' in line:
            final = cont +1
    texto = texto[comienzo: final]
    contador = 0
    for line in texto:
        try:
            a_escribir = line.split('=')
            parameter = a_escribir[0]
            valor = a_escribir[1]
            contador = contador + 1
            fits.setval(fitsFile, str(contador), value = valor, ext = 0, comment = parameter )
        except:
            pass
    #Comprobación de que el archivo FITS fue generado:
    check_fun = os.access(fitsFile, os.R_OK)
    if check_fun:
        if debug:
            print('All done')
        return True
    else:
        if debug:
            print('Something goes wrong')
        return False
