import mysql.connector

#Yhteyden luonti
yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database=input("Database NAME: "),
        user= input("Database USER: "),
        password= input("Database PASSWORD: "),
        autocommit=True
        )


#Yleisiä kyselyita varten, palauttaa arvon !listana jossa alkiot monikkoja!
def database_query(query):
    kursori = yhteys.cursor()
    kursori.execute(query)
    tulos = kursori.fetchall()
    return tulos

#Arvojen muuttamista varten ei palauta mitään
def database_update(query):
    kursori = yhteys.cursor()
    kursori.execute(query)
    return

def database_check_query(query):
    kursori = yhteys.cursor()
    kursori.execute(query)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        return True
    else:
        return False