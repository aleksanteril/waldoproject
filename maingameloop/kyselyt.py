


#Kysely jolla saadaan maan vihje jossa matkalaukku sijaitsee ICAO
#def query_country_hint(case_location):
#    sql_query_country_hint = (f"SELECT hint FROM country WHERE iso_country in("
#                          f"SELECT iso_country FROM airport WHERE ident = '{case_location}');")
#    return sql_query_country_hint

#UUSI kysely jolla saadaan vihje + ascii missä maassa matkalaukku sijaitsee
def query_country_hint_and_name(case_location):
    sql_query = (f"SELECT country.name, country.hint FROM country WHERE iso_country in ("
                 f"SELECT iso_country FROM airport WHERE ident = '{case_location}');")
    return sql_query


#Vakio kysely joka palauttaa maat, aakkosjärjestyksessä
query_countries = f"SELECT name FROM country WHERE continent = 'EU' ORDER BY name;"


#Kysely jolla saadaan parametri country avulla kyseisen maan lentokenttien ICAOT järjestyksessä large tyypistä alaspäin
def query_country_airports(country):
    sql_query_airports = (f"SELECT ident FROM airport, country "
                      f"WHERE airport.iso_country = country.iso_country and country.name ='{country}'"
                          f" ORDER BY CASE WHEN type = 'large_airport' THEN 1 WHEN type = 'medium_airport' THEN 2 WHEN type = 'small_airport' THEN 3 ELSE 4 END;")
    return sql_query_airports



#Kysely jolla saadaan etäisyys pelaajan ja jonkun toisen paikan välillä, float metreissä!
def query_distance_between_locations(playername, icao2):
    sql_query_distance = (f"SELECT ST_Distance_Sphere("
                                    f"ST_GeomFromText(("
                                    f"SELECT CONCAT('POINT (',longitude_deg, ' ',latitude_deg,')') FROM airport WHERE ident in(SELECT location FROM game WHERE id = '{playername}')), 4326), "
                                    f"ST_GeomFromText(("
                                    f"SELECT CONCAT('POINT (',longitude_deg, ' ',latitude_deg,')') FROM airport WHERE ident = '{icao2}'), 4326));")
    return sql_query_distance


#Kysely jolla päivitetään uusi käyttäjä tietokantaan
def query_new_username(username):
    sql_query_new_username = (f"INSERT INTO game (id, location) VALUES ('{username}', 'EFHK');")
    return sql_query_new_username

#Kysely jolla päivitetään tietyn pelaajan co2_total
def query_update_co2_total_player(username, co2_total):
    sql_query_insert_co2_total = (f"UPDATE game SET co2_consumed = {co2_total} WHERE id = '{username}';")
    return sql_query_insert_co2_total

#Kysely jolla tarkastetaan löytyykö nimi jo pelin tietokannasta
def query_check_username(username):
    sql_query_check_usernames = (f"SELECT id FROM game WHERE id = '{username}';")
    return sql_query_check_usernames


#Kysely jolla päivitetään pelaajan sijainti tietokantaan
def query_update_location(location, username):
    sql_query_insert_location = (f"UPDATE game SET location = ('{location}') WHERE id = '{username}';")
    return sql_query_insert_location

#Kysely jolla tarkistetaan löytyykö maa pelin maista, turha mutta jätetään varmuudeksi
#def query_check_country(country_name):
   #sql_query_check_country = (f"SELECT LOWER(name) FROM country WHERE name = '{country_name}' and continent = 'EU' and not name = 'Finland';")
   #return sql_query_check_country

#Kysely jolla saadaan käyttäjän maa LOWERcasena
def query_fetch_user_country(username):
    sql_query_fetch_user_country = (f"SELECT LOWER(name) FROM country WHERE iso_country in("
                                    f"SELECT iso_country FROM airport WHERE ident in("
                                    f"SELECT location FROM game WHERE id = '{username}'));")
    return sql_query_fetch_user_country
