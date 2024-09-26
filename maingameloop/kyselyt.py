


#Kysely jolla saadaan maan vihje jossa matkalaukku sijaitsee ICAO
def query_country_hint(case_location):
    sql_query_country_hint = (f"SELECT hint FROM country WHERE iso_country in("
                          f"SELECT iso_country FROM airport WHERE ident = '{case_location}');")
    return sql_query_country_hint




#Vakio kysely joka palauttaa maat
query_countries = f"SELECT name FROM country WHERE continent = 'EU';"



#Kysely jolla saadaan parametri country avulla kyseisen maan lentokenttien ICAOT
def query_country_airports(country):
    sql_query_airports = (f"SELECT ident FROM airport, country "
                      f"WHERE airport.iso_country = country.iso_country and country.name ='{country}';")
    return sql_query_airports



#Kysely joka palauttaa käyttäjän etäisyyden matkalaukkuun METREINÄ! #identtinen
def query_distance_from_goal(case_location, game_id):
    sql_query_distance_from_goal = (f"SELECT ST_Distance_Sphere("
                                    f"ST_GeomFromText(("
                                    f"SELECT CONCAT('POINT (',longitude_deg, ' ',latitude_deg,')') FROM airport WHERE ident in(SELECT location FROM game WHERE id = '{game_id}')), 4326), "
                                    f"ST_GeomFromText(("
                                    f"SELECT CONCAT('POINT (',longitude_deg, ' ',latitude_deg,')') FROM airport WHERE ident = '{case_location}'), 4326));")
    return sql_query_distance_from_goal

#Kysely jolla saadaan etäisyys pelaajan ja jonkun toisen paikan välillä #identtinen
def query_distance_between_locations(playername, icao2):
    sql_query_distance_from_goal = (f"SELECT ST_Distance_Sphere("
                                    f"ST_GeomFromText(("
                                    f"SELECT CONCAT('POINT (',longitude_deg, ' ',latitude_deg,')') FROM airport WHERE ident in(SELECT location FROM game WHERE id = '{playername}')), 4326), "
                                    f"ST_GeomFromText(("
                                    f"SELECT CONCAT('POINT (',longitude_deg, ' ',latitude_deg,')') FROM airport WHERE ident = '{icao2}'), 4326));")
    return sql_query_distance_from_goal



#Kysely jolla päivitetään uusi käyttäjä tietokantaan
def query_new_username(username):
    sql_query_new_username = (f"INSERT INTO game (id, location) VALUES ('{username}', 'EFHK');")
    return sql_query_new_username


#Kysely jolla tarkastetaan löytyykö nimi jo pelin tietokannasta
def query_check_username(username):
    sql_query_check_usernames = (f"SELECT id FROM game WHERE id = '{username}';")
    return sql_query_check_usernames


#Kysely jolla päivitetään pelaajan sijainti tietokantaan
def query_insert_location(location, username):
    sql_query_insert_location = (f"UPDATE game SET location = ('{location}') WHERE id = '{username}';")
    return sql_query_insert_location

#Kysely jolla tarkistetaan löytyykö maa pelin maista
def query_check_country(country_name):
    sql_query_check_usernames = (f"SELECT LOWER(name) FROM country WHERE name = '{country_name}';")
    return sql_query_check_usernames

#Kysely jolla saadaan käyttäjän maa LOWERcasena
def query_check_user_country(username):
    sql_query_check_user_country = (f"SELECT LOWER(name) FROM country WHERE iso_country in("
                                    f"SELECT iso_country FROM airport WHERE ident in("
                                    f"SELECT location FROM game WHERE id = '{username}'));")
    return sql_query_check_user_country