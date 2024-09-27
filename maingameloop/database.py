import mysql.connector

#Yhteyden luonti
yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database=input("Database: "),
        user=input("User: "),
        password=input("Password: "),
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

#Kyselyä varten, mutta haluamme vain ensimmäisen arvon tulokseen KÄYTÄ VAIN JOS TIEDÄT ETTÄ TULEE 1 ARVO
def database_query_fetchone(query):
    kursori = yhteys.cursor()
    kursori.execute(query)
    tulos = kursori.fetchone()
    return tulos


#Kyselyä varten jos tarvitsee tarkistaa löytyykö tieto esim.
def database_check_query(query):
    kursori = yhteys.cursor()
    kursori.execute(query)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        return True
    else:
        return False


# funktio tarkistaa onko käyttäjän syöttämä maa euroopassa
def travel_to_next(next_destination):
    query = "SELECT name FROM country WHERE name = %s AND continent = 'EU'"
    kursori = yhteys.cursor()
    kursori.execute(query, (next_destination,))
    tulos = kursori.fetchone()
    if tulos:
        print(f"Matkustat maahan: {next_destination}")
    else:
        print(f"Maata {next_destination} ei löytynyt Euroopasta.")

    return next_destination