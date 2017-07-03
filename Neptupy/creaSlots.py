#!/usr/bin/env python3

from os import listdir, environ
from main import imagen

# Change this line "clave" and orden (from 01 to 10):
orden = "01"
clave = "GEOMED"
NEPTUPY_ROOT = environ['NEPTUPY']
out_folder = NEPTUPY_ROOT + "slots/" + clave + "/"

# Indica que mira solo en la carpeta VGISS_orden
folder = NEPTUPY_ROOT + "VGISS_FITS/VGISS_82" + orden + "/"
lista_desorden = listdir(folder)
lista_gral = []
for arch in lista_desorden:
  if ("fits" in arch) and (clave in arch):
    lista_gral.append(arch)

# Ya está la lista con los nombres, ahora a revisar
# cuáles son los targets de cada fichero y ordenar
# en slots; que irán guardados en out_folder

slots = {}
for ffits in lista_gral:
  # Mirar en cada fichero el target y asignar
  imagenn = imagen(folder + ffits)
  target = imagenn.target
  try:
    slots[target].append(folder + ffits)
  except:
    slots[target] = []
    slots[target].append(folder + ffits)
# Ahora se van a organizar en grupos de a 20
# si?

# Comienza el guardado de los nombres de los slots
with open(out_folder + "slots" + orden + ".txt", "wb") as f:
  for i, target in enumerate(list(slots.keys())):
    slot_a = clave + "_" + orden + "_" + str(i) + "\n"
    f.write(slot_a.encode("utf-8"))
    f.write((target + "\n").encode("utf-8"))
    # Por cada elemento grabar en texto
    for archivo in slots[target]:
      a_guardar = archivo + "\n"
      f.write(a_guardar.encode("utf-8"))
    f.write("\n".encode("utf-8"))
