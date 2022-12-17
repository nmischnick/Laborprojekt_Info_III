import pymysql   #für die Verbindung zur MySQL-Datenbank
from datetime import datetime
import requests

#Verbindung zur Datenbank herstellen
try:
    connection = pymysql.connect(host='127.0.0.1',
                                  user='root',
                                  password='',
                                  )
    cursor = connection.cursor()
except:
    pass


def create_database(cursor, connection):
    #create database
    cursor.execute("CREATE DATABASE IF NOT EXISTS drucker_prozessdaten")  # Entweder Statement direkt einfügen
    cursor.execute("use drucker_prozessdaten")
    #create stats table
    sql = "CREATE TABLE IF NOT EXISTS `stats` (`stat_id` INT NOT NULL AUTO_INCREMENT , `time` DATETIME NOT NULL , `state` VARCHAR(20) NOT NULL , `temp_tool_i` FLOAT(30) NOT NULL , `temp_tool_s` FLOAT(30) NOT NULL , `temp_bed_i` FLOAT(30) NOT NULL , `temp_bed_s` FLOAT(30) NOT NULL , `free` BIGINT(30) NOT NULL , PRIMARY KEY (`stat_id`)) ENGINE = InnoDB;"
    cursor.execute(sql)
    #create files table
    sql = "CREATE TABLE IF NOT EXISTS `files` (`file_id` VARCHAR(100) NOT NULL , `display` VARCHAR(100) NOT NULL , `download` VARCHAR(100) NOT NULL , PRIMARY KEY (`file_id`)) ON DUPLICATE KEY UPDATE ENGINE = InnoDB;"
    cursor.execute(sql)
    #create jobs table
    sql = "CREATE TABLE IF NOT EXISTS `jobs` (`job_id` INT NOT NULL AUTO_INCREMENT , `display` VARCHAR(30) NOT NULL , `averagePrintTime` FLOAT(30) NOT NULL , `volume` FLOAT(30) NOT NULL , PRIMARY KEY (`job_id`)) ENGINE = InnoDB;"
    cursor.execute(sql)
    #create files table
    sql = "CREATE TABLE filetojob (job_id INT NOT NULL, file_id INT NOT NULL, FOREIGN KEY (job_id) REFERENCES jobs (job_id), FOREIGN KEY (file_id) REFERENCES files (file_id));"
    cursor.execute(sql)
    connection.commit()


#create_database()

#cursor = create_connection()[0]
cursor.execute("use drucker_prozessdaten")
#connection = create_connection()[1]

def get_job_id(jobs):
    display = str(jobs["display"])
    date = str(jobs["date"])

    sql = "SELECT job_id FROM jobs WHERE date ='" + date + "' AND display = '"+display+"';"

    cursor.execute(sql)
    result = cursor.fetchone()

    return result

def get_hash_from_display_date(jobs):
    display = str(jobs["display"])
    date = str(jobs["date"])

    sql = "SELECT file_id FROM files WHERE date ='" + date + "' AND display = '" + display + "';"

    cursor.execute(sql)
    result = cursor.fetchone()

    return result


#stats TABLE
def to_database_stats(printer, files):
    dt = str(datetime.now())
    state = str(printer["state"])
    temp_tool_i = str(printer["temp_tool_i"])
    temp_tool_s = str(printer["temp_tool_s"])
    temp_bed_i = str(printer["temp_bed_i"])
    temp_bed_s = str(printer["temp_bed_s"])
    free = str(files[0]["free"])
    #job_id = str(5)

    #get current job
    sql = "SELECT job_id FROM jobs ORDER BY job_id DESC LIMIT 1"
    cursor.execute(sql)
    result = cursor.fetchone()
    job_id = str(result[0])



    sql = "INSERT INTO `stats` (`stat_id`, `time`, `state`, `temp_tool_i`, `temp_tool_s`, `temp_bed_i`, `temp_bed_s`, `free`, `job`) " \
          "VALUES (NULL, '"+dt+"', '"+state+"', '"+temp_tool_i+"', '"+temp_tool_s+"', '"+temp_bed_i+"', '"+temp_bed_s+"', '"+free+"', '"+job_id+"');"

    cursor.execute(sql)
    connection.commit()


#files TABLE
def to_database_files(files):
    for file in files:
        file_id = str(file["hash"])
        display = str(file["display"])
        download = str(file["download"])
        date = str(file["date"])

        sql = "INSERT IGNORE INTO `files` (`file_id`, `display`, `date`, `download`) VALUES ('"+file_id+"', '"+display+"', '"+date+"','"+download+"');"

        cursor.execute(sql)
        connection.commit()



#jobs TABLE
def to_database_jobs(jobs):
    hash = str(get_hash_from_display_date(jobs)[0])
    averagePrintTime = str(jobs["averagePrintTime"])
    volume = str(jobs["volume"])

    #checking if job with hash is already in job table (no duplicate files possible)
    sql = "SELECT file FROM jobs WHERE file ='" + hash + "';"
    cursor.execute(sql)
    if cursor.fetchone() is None:

        sql = "INSERT IGNORE INTO `jobs` (`job_id`, `file`, `averagePrintTime`, `volume`) VALUES (NULL, '"+hash+"', '"+averagePrintTime+"', '"+volume+"');"

        cursor.execute(sql)
        connection.commit()

    else: #wenn hash schonmal in jobs war gucke, ob der letzte job auch hash war, wenn nicht füge hinzu
        sql = "SELECT file FROM jobs ORDER BY job_id DESC LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchone()
        file = str(result[0])

        if file != hash:
            sql = "INSERT IGNORE INTO `jobs` (`job_id`, `file`, `averagePrintTime`, `volume`) VALUES (NULL, '" + hash + "', '" + averagePrintTime + "', '" + volume + "');"

            cursor.execute(sql)
            connection.commit()




def to_database_all(printer, files, jobs):

    to_database_jobs(jobs) #muss zuerst sonst bekommt stats keine job_id
    to_database_stats(printer, files)
    to_database_files(files)

def load_gcode(dateiname):
    '''
    Lädt zu gegebenem Dateiname den GCode herunter

    :param dateiname: Name der Datei zu der der GCode heruntergeladen werden soll
    :return: None
    '''

    sql = "SELECT download FROM files WHERE display ='"+dateiname+"';"

    cursor.execute(sql)
    result = cursor.fetchone()

    r = requests.get(result[0], allow_redirects=True)

    open(dateiname, 'wb').write(r.content)


def storage_progress(von, bis):
    '''
    Gibt 2 Listen (zeitpunkt, wert) zurück, um den Verlauf des freien Speicherplatzes auf dem Server zu plotten

    :param von: Zeitpunkt, ab dem der Verlauf beginnen soll
    :param bis: Zeitpunkt, an dem der Verlauf enden soll
    :return: 2 Listen mit Zeitpunkt und Wert
    :rtype: list
    '''

    #bis = datetime.now()
    #von = datetime(2020, 1, 1)

    times = []
    storage = []

    sql = "SELECT time, free FROM stats WHERE time < '" + str(bis) + "' AND time > '" + str(von) + "' ORDER BY time ASC;" #Alle zeit und speicher werte in Zeitraum von-bis

    cursor.execute(sql)
    result = cursor.fetchall()

    for i in result:
        times.append(i[0])
        storage.append(i[1])
        #print(i[0], i[1])

    return times, storage


def count_states(von, bis):
    '''
    Ermittelt, wie oft der Drucker im Zeitraum x in einem der Stati (Bereit, Aus, Druckt, Pausiert, Störung) war

    :param von: Zeitpunkt, ab dem der Verlauf beginnen soll
    :param bis: Zeitpunkt, an dem der Verlauf enden soll
    :return: Dictionary mit status als key und Anzahl als value
    :rtype: dict
    '''

    states = [] #Liste für alle werte
    state_dict = {}#{"error": 0, "ready": 0, "paused": 0, "printing": 0} #Ergebnis dict


    sql = "SELECT state FROM stats WHERE time < '" + str(bis) + "' AND time > '" + str(von) + "';" #alle states in Zeitraum von-bis

    cursor.execute(sql)
    result = cursor.fetchall()


    for i in result: #füge Ergebnisse in eine Liste
        states.append(i[0])


    #states = ["error", "paused", "error", "error", "paused", "printing", "printing", "error", "error"] #test liste

    for i in range(len(states)-1):
        if states[i] != states[i+1]: #wenn unterschiedlich füge wert hinzu
            if str(states[i]) not in state_dict:
                state_dict[str(states[i])] = 1
            else:
                state_dict[str(states[i])] += 1

    if str(states[-1]) not in state_dict: #um letzen wert hinzuzufügen
        state_dict[str(states[-1])] = 1
    else:
        state_dict[str(states[-1])] += 1

    return state_dict

def get_all_jobs():
    '''
    Gibt alle Druckaufträge wieder
    :return: tuple, gefüllt mit tuplen Bsp.: ((job_id, dateiname, downloadlink),(...))
    :rtype: tuple
    '''

    sql = "SELECT job_id, display, download FROM jobs INNER JOIN files ON jobs.file = files.file_id"

    cursor.execute(sql)
    result = cursor.fetchall()

    return(result)

def temp_progress(job_id):
    '''
    Gibt die Temperaturen eines Druckauftrages + Zeit(datetime) wieder
    :param job_id: identifiziert den geforderten job (welche man aus get_all_jobs() bekommt)
    :return: tuple, gefüllt mit tuplen Bsp.: ((time, temp_tool_i, temp_tool_s, temp_bed_i, temp_bed_s),(...))
    :rtype: tuple
    '''

    sql = "SELECT time, temp_tool_i, temp_tool_s, temp_bed_i, temp_bed_s FROM stats WHERE job ='" + str(job_id) + "';"

    cursor.execute(sql)
    result = cursor.fetchall()

    return(result)

