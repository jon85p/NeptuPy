#!/usr/bin/env python3
import os
import sqlite3
from astropy.io import fits

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def genDB(file_name, NEPTUPY_ROOT):
    # Generate and fill the database!
    conn = sqlite3.connect(file_name)
    c = conn.cursor()
    # Tables of db
    c.execute('CREATE TABLE targets(id_tar int, name_tar varchar(50), CONSTRAINT pk_tar PRIMARY KEY (id_tar), CONSTRAINT Ut UNIQUE (name_tar))')
    c.execute('CREATE TABLE filters(id_fil int, name_fil varchar(50), CONSTRAINT pk_fil PRIMARY KEY (id_fil), UNIQUE (name_fil))')
    c.execute('CREATE TABLE cams(id_cam int, name_cam varchar(50), CONSTRAINT pk_cam PRIMARY KEY (id_cam), UNIQUE (name_cam))')
    c.execute('CREATE TABLE types(id_type int, name_type varchar(10), CONSTRAINT pk_type PRIMARY KEY(id_type))')
    c.execute('CREATE TABLE imgs(id_img varchar(10), img_num varchar(20), id_tar1 int, id_fil1 int, expo_time float, start_time datetime, stop_time datatime, id_cam1 int, location varchar(100), id_type1 int, CONSTRAINT pk_img PRIMARY KEY (id_img),CONSTRAINT fk_type FOREIGN KEY (id_type1) REFERENCES types(id_type), CONSTRAINT fk_tar FOREIGN KEY (id_tar1) REFERENCES targets(id_tar), CONSTRAINT fk_fil FOREIGN KEY (id_fil1) REFERENCES filters(id_fil), CONSTRAINT fk_cam FOREIGN KEY (id_cam1) REFERENCES cams(id_cam))')
    targets = [(1, 'NEREID'), (2, 'NEPTUNE'), (3, 'SKY'), (4, 'TRITON'), (5, 'DARK'),
               (6, 'STAR'), (7, 'PROTEUS'), (8, 'N RINGS'), (9, 'SIGMA SGR'), (10, 'LARISSA'),
               (11, 'BETACMA'), (12, 'VEGA'), (13, 'ORION'), (14, 'PLAQUE'), (15, 'CAL LAMPS'),
               (16, 'PLEIADES'), (17, 'SCORPIUS')]
    targets_dict = dict(targets)
    cams = [(1, 'IMAGING SCIENCE SUBSYSTEM - NARROW ANGLE'),
            (2, 'IMAGING SCIENCE SUBSYSTEM - WIDE ANGLE')]
    cams_dict = dict(cams)
    filters = [(1, 'CLEAR'), (2, "ORANGE"), (3, "CH4_JS"),
               (4, "UV"), (5, "VIOLET"), (6, "GREEN"),
               (7, "BLUE"), (8, "CH4_U"), (9, "SODIUM")]
    filters_dict = dict(filters)
    types = [(1, 'RAW'), (2, 'CALIB'), (3, 'GEOMED'), (4, 'CLEANED')]
    types_dict = dict(types)
    c.executemany('INSERT INTO targets VALUES (?, ?)', targets)
    c.executemany('INSERT INTO cams VALUES (?, ?)', cams)
    c.executemany("INSERT INTO filters VALUES (?, ?)", filters)
    c.executemany("INSERT INTO types VALUES (?, ?)", types)
    # Now, the images!
    list_f = [os.path.join(dp, f) for dp, dn, filenames in os.walk(NEPTUPY_ROOT + "VGISS_FITS") for f in filenames if os.path.splitext(f)[1] == '.fits']
    for image in list_f:
     try:
      fit_i = fits.open(image)
      header = fit_i[0].header
      camera = find_between(header[9], '"', '"')
      id_camera = list(cams_dict.values()).index(camera) + 1
      target = find_between(header[12], '"', '"')
      id_target = list(targets_dict.values()).index(target) + 1
      filterr = find_between(header[21], '"', '"')
      id_filter = list(filters_dict.values()).index(filterr) + 1
      typee = find_between(image[-20::], "_", ".fits")
      id_type = list(types_dict.values()).index(typee) + 1
#      id_img = find_between(header[13], '"', '"') + typee # Avoid repeated ID for types
      id_img = image.split('/')[-1].split('.')[0]
      num_img = find_between(header[14], '"', '"')
      expo_t = find_between(header[23], " ", ' <')
      start_t = header[24][1::]
      stop_t = header[25][1::]
      # Save!
      image_loc = image.replace(NEPTUPY_ROOT, "")
      sql = (id_img, num_img, id_target, id_filter, expo_t, start_t, stop_t, id_camera, image_loc, id_type)
      c.execute("INSERT INTO imgs VALUES (?,?,?,?,?,?,?,?,?,?)", sql)
     except Exception as e:
      print(image, str(e))
    conn.commit()
def main():
    # Check database existence
    NEPTUPY_ROOT = os.environ["NEPTUPY"]
    file_name = NEPTUPY_ROOT + 'general.db'
    if not os.path.exists(file_name):
      genDB(file_name, NEPTUPY_ROOT)
    else:
      print("Database already exists!\n Quitting")
      exit(0)

if __name__ == "__main__":
    main()
