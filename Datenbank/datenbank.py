import pymysql   #für die Verbindung zur MySQL-Datenbank
from test_datenbank import sample_data_printer, sample_data_files, sample_data_job
from datetime import datetime
import requests

#Verbindung zur Datenbank herstellen
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='',
                             )


#Cursor zur Abfrage von Daten
cursor = connection.cursor()

def create_database():
    #create database
    cursor.execute("CREATE DATABASE IF NOT EXISTS drucker_prozessdaten")  # Entweder Statement direkt einfügen
    cursor.execute("use drucker_prozessdaten")
    #create stats table
    sql = "CREATE TABLE IF NOT EXISTS `stats` (`stat_id` INT NOT NULL AUTO_INCREMENT , `time` DATETIME NOT NULL , `state` VARCHAR(20) NOT NULL , `temp_tool_i` FLOAT(30) NOT NULL , `temp_tool_s` FLOAT(30) NOT NULL , `temp_bed_i` FLOAT(30) NOT NULL , `temp_bed_s` FLOAT(30) NOT NULL , `free` BIGINT(30) NOT NULL , PRIMARY KEY (`stat_id`)) ENGINE = InnoDB;"
    cursor.execute(sql)
    #create files table
    sql = "CREATE TABLE IF NOT EXISTS `files` (`file_id` VARCHAR(100) NOT NULL , `display` VARCHAR(100) NOT NULL , `download` VARCHAR(100) NOT NULL , PRIMARY KEY (`file_id`)) ENGINE = InnoDB;"
    cursor.execute(sql)
    #create jobs table
    sql = "CREATE TABLE IF NOT EXISTS `jobs` (`job_id` INT NOT NULL AUTO_INCREMENT , `display` VARCHAR(30) NOT NULL , `averagePrintTime` FLOAT(30) NOT NULL , `volume` FLOAT(30) NOT NULL , PRIMARY KEY (`job_id`)) ENGINE = InnoDB;"
    cursor.execute(sql)

create_database()


#stats TABLE
def to_database_stats(printer, files):
    dt = str(datetime.now())
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
def to_database_files(files):
    for file in files:
        file_id = str(file["hash"])
        display = str(file["display"])
        download = str(file["download"])

        sql = "INSERT IGNORE INTO `files` (`file_id`, `display`, `download`) VALUES ('"+file_id+"', '"+display+"', '"+download+"');"

        cursor.execute(sql)
        connection.commit()

#jobs TABLE
def to_database_jobs(jobs):
    display = str(jobs["display"])
    averagePrintTime = str(jobs["averagePrintTime"])
    volume = str(jobs["volume"])

    sql = "INSERT INTO `jobs` (`job_id`, `display`, `averagePrintTime`, `volume`) VALUES (NULL, '"+display+"', '"+averagePrintTime+"', '"+volume+"');"

    cursor.execute(sql)
    connection.commit()



def to_database_all(printer, files, jobs):

    to_database_jobs(jobs)
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

    #return result[0]

load_gcode("testfile")

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