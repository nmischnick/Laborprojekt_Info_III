import pymysql   #für die Verbindung zur MySQL-Datenbank
from test_datenbank import sample_data_printer, sample_data_files, sample_data_job
from datetime import datetime

#Verbindung zur Datenbank herstellen
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='',
                             )


#Cursor zur Abfrage von Daten
cursor = connection.cursor()

# Datenbank auswählen
sql="use drucker_prozessdaten"
cursor.execute(sql)

dt = str(datetime.now())

printer = sample_data_printer()
files = sample_data_files()
jobs = sample_data_job()


#stats TABLE
def to_database_stats():
    state = str(printer["state"])
    temp_tool_i = str(printer["temp_tool_i"])
    temp_tool_s = str(printer["temp_tool_s"])
    temp_bed_i = str(printer["temp_bed_i"])
    temp_bed_s = str(printer["temp_bed_s"])
    free = str(files["free"])

    sql = "INSERT INTO `stats` (`stat_id`, `time`, `state`, `temp_tool_i`, `temp_tool_s`, `temp_bed_i`, `temp_bed_s`, `free`) " \
          "VALUES (NULL, '"+dt+"', '"+state+"', '"+temp_tool_i+"', '"+temp_tool_s+"', '"+temp_bed_i+"', '"+temp_bed_s+"', '"+free+"');"

    cursor.execute(sql)
    connection.commit()


#files TABLE
def to_database_files():
    for file in files:
        file_id = str(file["hash"])
        display = str(file["display"])
        download = str(file["download"])

        sql = "INSERT IGNORE INTO `files` (`file_id`, `display`, `download`) VALUES ('"+file_id+"', '"+display+"', '"+download+"');"

        cursor.execute(sql)
        connection.commit()

#jobs TABLE
def to_database_jobs():
    display = str(jobs["display"])
    averagePrintTime = str(jobs["averagePrintTime"])
    volume = str(jobs["volume"])

    sql = "INSERT INTO `jobs` (`job_id`, `display`, `averagePrintTime`, `volume`) VALUES (NULL, '"+display+"', '"+averagePrintTime+"', '"+volume+"');"

    cursor.execute(sql)
    connection.commit()


to_database_files()

def load_gcode(dateiname):

    sql = "SELECT download FROM files WHERE display ='"+dateiname+"';"

    cursor.execute(sql)
    result = cursor.fetchone()

    return result[0]



def storage_progress(von, bis):

    #bis = datetime.now()
    #von = datetime(2020, 1, 1)

    times = []
    storage = []

    sql = "SELECT time, free FROM stats WHERE time < '" + str(bis) + "' AND time > '" + str(von) + "' ORDER BY time ASC;"

    cursor.execute(sql)
    result = cursor.fetchall()

    for i in result:
        times.append(i[0])
        storage.append(i[1])
        #print(i[0], i[1])