#!/usr/bin/env python3
import os
import sys
from ImportPDS import pds2fits

def name_wo_ext(file_route):
    '''
    Return filename without and with extension
    '''
    wo_ext = (file_route.split('/'))[-1].split('.')[-2]
    wi_ext = (file_route.split('/'))[-1]
    return (wo_ext, wi_ext)

def main():
    #Folder with files to be converted:
    NEPTUPY_ROOT = os.environ["NEPTUPY"]
    resources = NEPTUPY_ROOT + 'VGISS/'
    #Output folder:
    salida = NEPTUPY_ROOT + 'VGISS_FITS/'
    #Search start inside the resources folder
    sublist_1 = os.listdir(resources)
    sublist_2 = [] #CXXXXXXX Folders
    for folder in sublist_1:
        #For each VGISSXX save CXXXXXXX folders on sublist_2 list
        CXXXXXXX = os.listdir(resources + folder + '/DATA')
        for fold in CXXXXXXX:
            sublist_2.append([fold, folder])
    sublist_3 = [] #This list will contain .LBL and .IMG filenames
    for cx in sublist_2:
        #For each CXXXXXXX folder, append append all .IMG files
        #(if have a .LBL file associated)
        try:
            CXXXXXXX_list = os.listdir(resources + cx[1] + '/DATA/' + cx[0])
        except:
            pass
        for _file_ in CXXXXXXX_list:
            #For each _file_ watch if must be added to sublist_3
            if '.LBL' in _file_:
                #If have a LBL file, check for IMG.
                sin, con = name_wo_ext(_file_)
                if (sin + '.IMG') in CXXXXXXX_list:
                    sublist_3.append(resources + cx[1] + '/DATA/' + cx[0] + '/' + _file_)
    mostra = sublist_3[5485].split('/')
    mostra = mostra[8]
    print(mostra)
    print('Will be converted' ,len(sublist_3), 'files')
    #Start conversion
    size = len(sublist_3)
    counter = 1
    for pds in sublist_3:
        #Conversion:
        mostra = pds.split('/')
        subsalida = salida + mostra[8] + '/'#Output subfolder
        sin, con = name_wo_ext(pds) # Output filename
        _file__fits = sin + '.fits'
        try:
            pds2fits(pds, subsalida + _file__fits, ignore_existence = False)
        except:
            print('Problem with',pds)
        print(counter, 'of', size)
        counter = counter + 1
if __name__ == '__main__':
    main()
