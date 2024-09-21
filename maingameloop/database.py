import mysql.connector

yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user= input("Database USER: "),
        password= input("Database PASSWORD: "),
        autocommit=True
        )