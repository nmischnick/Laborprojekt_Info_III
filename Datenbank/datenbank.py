import pymysql  # für die Verbindung zur MySQL-Datenbank
from datetime import datetime
import requests
from collections import Counter

# Verbindung zur Datenbank herstellen

try:
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='',
                                 )
    cursor = connection.cursor()
except:
    pass


def create_database():
    """
    Erstellt die Datenbank und die dazugehörigen Tabellen

    :author: Luis Klimpke
    :return: None
    """

    cursor.execute("CREATE DATABASE IF NOT EXISTS drucker_prozessdaten2")  # Entweder Statement direkt einfügen
    cursor.execute("use drucker_prozessdaten2")

    # create files table
    sql = """
            CREATE TABLE IF NOT EXISTS `files` (
                `file_id` varchar(30) NOT NULL,
                `display` varchar(30) NOT NULL,
                `download` varchar(30) NOT NULL,
                `date` datetime(6) NOT NULL,
                PRIMARY KEY (`file_id`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
            """
    cursor.execute(sql)

    # create jobs table
    sql = """
            CREATE TABLE IF NOT EXISTS `jobs` (
                `job_id` int(10) NOT NULL AUTO_INCREMENT,
                `time` datetime(6) NOT NULL,
                `file` varchar(30) NOT NULL,
                `averagePrintTime` float NOT NULL,
                `volume` float NOT NULL,
                PRIMARY KEY (`job_id`),
                KEY `file_id_zu_file` (`file`),
                CONSTRAINT `file_id_zu_file` FOREIGN KEY (`file`) REFERENCES `files` (`file_id`)
            ) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
            """
    cursor.execute(sql)
    connection.commit()

    # create stats table
    sql = """
        CREATE TABLE IF NOT EXISTS `stats` (
            `stat_id` int(10) NOT NULL AUTO_INCREMENT,
            `time` datetime(6) NOT NULL,
            `state` varchar(10) NOT NULL,
            `temp_tool_i` float NOT NULL,
            `temp_tool_s` float NOT NULL,
            `temp_bed_i` float NOT NULL,
            `temp_bed_s` float NOT NULL,
            `free` bigint(30) NOT NULL,
            `job` int(10) NOT NULL,
            PRIMARY KEY (`stat_id`),
            KEY `job` (`job`),
            CONSTRAINT `stats_ibfk_1` FOREIGN KEY (`job`) REFERENCES `jobs` (`job_id`)
        ) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
        """
    cursor.execute(sql)


# create_database()

# cursor.execute("use drucker_prozessdaten2")


def get_hash_from_display_date(jobs):
    """
    Liefert den hash der Datei zurück(Primary Key) zu dann geg. Namen und Datum der Datei aus jobs Tabelle.
    Nötig für Verknüpfung von files und jobs

    :author: Luis Klimpke
    :param jobs: jobs-json-daten
    :return: file_id bzw der hash der geforderten Datei
    :rtype: str
    """
    display = str(jobs["display"])
    date = str(jobs["date"])

    sql = "SELECT file_id FROM files WHERE date ='" + date + "' AND display = '" + display + "';"

    cursor.execute(sql)
    result = cursor.fetchone()

    return str(result)


# stats TABLE
def to_database_stats(printer, files):
    """
    Fügt die Daten aus dem geg. Dicts in stats Tabelle ein

    :author: Luis Klimpke
    :param printer: printer-json-daten
    :param files: files-json-daten
    :return: None
    """
    dt = str(datetime.now())
    state = str(printer["state"])
    temp_tool_i = str(printer["temp_tool_i"])
    temp_tool_s = str(printer["temp_tool_s"])
    temp_bed_i = str(printer["temp_bed_i"])
    temp_bed_s = str(printer["temp_bed_s"])
    free = str(files[0]["free"])
    # job_id = str(5)

    # get current job
    sql = "SELECT job_id FROM jobs ORDER BY job_id DESC LIMIT 1"
    cursor.execute(sql)
    result = cursor.fetchone()
    job_id = str(result[0])

    sql = "INSERT INTO `stats` (`stat_id`, `time`, `state`, `temp_tool_i`, `temp_tool_s`, `temp_bed_i`, `temp_bed_s`, `free`, `job`) " \
          "VALUES (NULL, '" + dt + "', '" + state + "', '" + temp_tool_i + "', '" + temp_tool_s + "', '" + temp_bed_i + "', '" + temp_bed_s + "', '" + free + "', '" + job_id + "');"

    cursor.execute(sql)
    connection.commit()


# files TABLE
def to_database_files(files):
    """
    Fügt die Daten aus dem geg. Dict in files Tabelle ein

    :author: Luis Klimpke
    :param files: files-json-daten
    :return: None
    """
    for file in files:
        file_id = str(file["hash"])
        display = str(file["display"])
        download = str(file["download"])
        date = str(file["date"])

        sql = "INSERT IGNORE INTO `files` (`file_id`, `display`, `date`, `download`) VALUES ('" + file_id + "', '" + display + "', '" + date + "','" + download + "');"

        cursor.execute(sql)
        connection.commit()


# jobs TABLE
def to_database_jobs(jobs):
    """
    Fügt die Daten aus dem geg. Dict in jobs Tabelle ein

    :author: Luis Klimpke
    :param jobs: jobs-json-daten
    :return: None
    """

    hash = str(get_hash_from_display_date(jobs)[0])
    averagePrintTime = str(jobs["averagePrintTime"])
    volume = str(jobs["volume"])
    dt = str(datetime.now())

    # checking if job with hash is already in job table (no printing same file after another possible)
    sql = "SELECT file FROM jobs WHERE file ='" + hash + "';"
    cursor.execute(sql)
    if cursor.fetchone() is None:

        sql = "INSERT IGNORE INTO `jobs` (`job_id`, `file`, `averagePrintTime`, `volume`, `date`) VALUES (NULL, '" + hash + "', '" + averagePrintTime + "', '" + volume + "', '" + dt + "');"

        cursor.execute(sql)
        connection.commit()

    else:  # wenn hash schonmal in jobs war gucke, ob der letzte job auch hash war, wenn nicht füge hinzu
        sql = "SELECT file FROM jobs ORDER BY job_id DESC LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchone()
        file = str(result[0])

        if file != hash:
            sql = "INSERT IGNORE INTO `jobs` (`job_id`, `file`, `averagePrintTime`, `volume`, `date`) VALUES (NULL, '" + hash + "', '" + averagePrintTime + "', '" + volume + "', '" + dt + "');"
            cursor.execute(sql)
            connection.commit()


def to_database_all(files, jobs, printer):
    '''
    Fügt alle Funktionen zusammen, die json-Daten in Datenbank hochladen

    :author: Luis Klimpke
    :param files: files-json-daten
    :param jobs: jobs-json-daten
    :param printer: printer-json-daten
    :return: None
    '''

    to_database_files(files)
    to_database_jobs(jobs)  # muss zuerst sonst bekommt stats keine job_id
    to_database_stats(printer, files)


def load_gcode(dateiname):
    """
    Lädt zu gegebenem Dateiname den GCode herunter

    :author: Luis Klimpke
    :param dateiname: Name der Datei zu der der GCode heruntergeladen werden soll
    :return: None
    """

    sql = "SELECT download FROM files WHERE display ='" + dateiname + "';"

    cursor.execute(sql)
    result = cursor.fetchone()

    r = requests.get(result[0], allow_redirects=True)

    open(dateiname, 'wb').write(r.content)


def storage_progress(von, bis):
    """
    Gibt 2 Listen (zeitpunkt, wert) zurück, um den Verlauf des freien Speicherplatzes auf dem Server zu plotten

    :author: Luis Klimpke
    :param von: Zeitpunkt, ab dem der Verlauf beginnen soll
    :param bis: Zeitpunkt, an dem der Verlauf enden soll
    :return: 2 Listen mit Zeitpunkt und Wert
    :rtype: list
    """

    # bis = datetime.now()
    # von = datetime(2020, 1, 1)

    times = []
    storage = []

    sql = "SELECT time, free FROM stats WHERE time < '" + str(bis) + "' AND time > '" + str(
        von) + "' ORDER BY time ASC;"  # Alle zeit und speicher werte in Zeitraum von-bis

    cursor.execute(sql)
    result = cursor.fetchall()

    for i in result:
        times.append(i[0])
        storage.append(i[1])
        # print(i[0], i[1])

    return times, storage


def count_states(von, bis):
    """
    Ermittelt, wie oft der Drucker im Zeitraum x in einem der Stati (Bereit, Aus, Druckt, Pausiert, Störung) war

    :author: Luis Klimpke
    :param von: Zeitpunkt, ab dem der Verlauf beginnen soll
    :param bis: Zeitpunkt, an dem der Verlauf enden soll
    :return: Dictionary mit status als key und Anzahl als value
    :rtype: dict
    """

    states = []  # Liste für alle werte
    state_dict = {}  # {"error": 0, "ready": 0, "paused": 0, "printing": 0} #Ergebnis dict

    sql = "SELECT state FROM stats WHERE time < '" + str(bis) + "' AND time > '" + str(
        von) + "';"  # alle states in Zeitraum von-bis

    cursor.execute(sql)
    result = cursor.fetchall()

    for i in result:  # füge Ergebnisse in eine Liste
        states.append(i[0])

    # states = ["error", "paused", "error", "error", "paused", "printing", "printing", "error", "error"] #test liste

    for i in range(len(states) - 1):
        if states[i] != states[i + 1]:  # wenn unterschiedlich füge wert hinzu
            if str(states[i]) not in state_dict:
                state_dict[str(states[i])] = 1
            else:
                state_dict[str(states[i])] += 1

    if str(states[-1]) not in state_dict:  # um letzen wert hinzuzufügen
        state_dict[str(states[-1])] = 1
    else:
        state_dict[str(states[-1])] += 1

    return state_dict


def get_all_jobs():
    """
    Gibt alle Druckaufträge wieder

    :author: Luis Klimpke
    :return: tuple, gefüllt mit tuplen Bsp.: ((job_id, dateiname, downloadlink),(...))
    :rtype: tuple
    """

    sql = "SELECT job_id, display, download FROM jobs INNER JOIN files ON jobs.file = files.file_id"

    cursor.execute(sql)
    result = cursor.fetchall()

    return result


def temp_progress(job_id):
    """
    Gibt die Temperaturen eines Druckauftrages + Zeit(datetime) wieder

    :author: Luis Klimpke
    :param job_id: identifiziert den geforderten job (welche man aus get_all_jobs() bekommt)
    :return: tuple, gefüllt mit tuplen Bsp.: ((time, temp_tool_i, temp_tool_s, temp_bed_i, temp_bed_s),(...))
    :rtype: tuple
    """

    sql = "SELECT time, temp_tool_i, temp_tool_s, temp_bed_i, temp_bed_s FROM stats WHERE job ='" + str(job_id) + "';"

    cursor.execute(sql)
    result = cursor.fetchall()

    return(result)


def object_count_period(von, bis, file):
    """
    Ermittelt, wie oft ein bestimmter Job erfolgreich ausgerührt wurde

    :author: Marcel Lindwedel
    :param von: Zeitpunkt, ab dem der Verlauf beginnen soll
    :param bis: Zeitpunkt, an dem der Verlauf enden soll
    :param file: bestimmte Objektart
    """

    #file = "1"

    anzahl = []

    sql = "SELECT file, time FROM jobs WHERE time < '" + str(bis) + "' AND time > '" + str(von) + "' ORDER BY time ASC;"

    cursor.execute(sql)
    result = cursor.fetchall()

    for i in result:
        anzahl.append(i[0])

    anzahl_all = (Counter(anzahl))
    print("Es wurden von Objekt", file, "insgesamt", anzahl_all[file], "Stücke gefertigt")

def average_volume_period(von, bis):
    """
    Ermittelt, wie viel Volumen in einem bestimmten Zeitraum verbraucht wurde

    :author: Marcel Lindwedel
    :param von: Zeitpunkt, ab dem der Verlauf beginnen soll
    :param bis: Zeitpunkt, an dem der Verlauf enden soll
    """

    volume = []

    sql = "SELECT time, volume FROM jobs WHERE time < '" + str(bis) + "' AND time > '" + str(von) + "' ORDER BY time ASC;"

    cursor.execute(sql)
    result = cursor.fetchall()

    for i in result:
        volume.append(i[1])

    print(sum(volume) / len(volume))

def average_print_time():
    """
    Ermittelt, wie die durchschnittliche Durckzeit eines Objektes ist

    :author: Marcel Lindwedel
    """

    job_id = []
    averagePrintTime = []

    counter = 0

    sql = "SELECT job_id, averagePrintTime FROM jobs;"

    cursor.execute(sql)
    result = cursor.fetchall()

    for i in result:
        job_id.append(i[0])
        averagePrintTime.append(i[1])

    while counter < len(result):
        print("Job:", job_id[counter], "Hat eine durchschnittliche Druckdauer von:", averagePrintTime[counter])
        counter += 1
