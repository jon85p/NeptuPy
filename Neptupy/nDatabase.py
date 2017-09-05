import sqlite3
import os
NR = os.environ["NEPTUPY"]
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

def searchDB(target=None,expo_1=None, expo_2=None, date_st=None, date_sp=None, filterr=None,
             typee=None, camera=None):
	'''
	Search for location of fits files according a set of search conditions:

	params
	target: str Target to lookup, default None, ex = 'NEPTUNE'
	expo_1: str Minimum expo time (seconds), default None, ex = '12'
	expo_2: str Maximum expo time (seconds), default None, ex = '20'
	date_st: str Initial date of search, default None, ex = '1989-08-29T13:47:42.56'
	date_sp: str Stop date of search, default None, ex = '1989-09-29T13:47:42.56'
	filterr: str Filter to look up, default None, ex = 'UV'
	typee: str Type of image, default None, ex = 'GEOMED'
	camera: str Camera of lookup, default None, ex = 'IMAGING SCIENCE SUBSYSTEM - WIDE ANGLE'

	return
	A strings list with location of located images	
	'''
	if not os.path.exists(NR + "general.db"):
		print("Database general.db not found!, generate it with createDatabase.py firsts")
		exit(1)
	conn = sqlite3.connect(NR + "general.db")
	c = conn.cursor()
	sql = "SELECT location FROM imgs WHERE(id_tar1 AND id_fil1 AND expo_t1 AND expo_t2 AND start_time1 AND start_time2 AND id_type1 AND id_cam1)"
	# Replace strings of query with params data
	if target:
		sql = sql.replace("id_tar1", "id_tar1="+str(list(targets_dict.values()).index(target)+1))
	if filterr:
		sql = sql.replace("id_fil1", "id_fil1="+str(list(filters_dict.values()).index(filterr)+1))
	if typee:
		sql = sql.replace("id_type1", "id_type1="+str(list(types_dict.values()).index(typee)+1))
	if camera:
		sql = sql.replace("id_cam1", "id_cam1=" + str(list(cams_dict.values()).index(cam) + 1))
	# Now the times!
	if expo_1:
		sql = sql.replace("expo_t1", "expo_time >= " + expo_1)
	else:
		sql = sql.replace("expo_t1", "expo_time")
	if expo_2:
		sql = sql.replace("expo_t2", "expo_time <= " + expo_2)
	else:
		sql = sql.replace("expo_t2", "expo_time")
	if date_st:
		sql = sql.replace("start_time1", "start_time >= " + date_st)
	else:
		sql = sql.replace("start_time1", "start_time")
	if date_sp:
		sql = sql.replace("start_time2", "start_time <= " + date_sp)
	else:
		sql = sql.replace("start_time2", "start_time")
	# SQL query done!
	list_out = []
	c.execute(sql)
	for row in c:
		list_out.append(NR + str(row)[2:-3])
	return list_out







	
	
	
