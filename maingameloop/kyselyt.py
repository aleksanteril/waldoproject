

#KYSELYT PELIN LOGIIKKAA VARTEN #############################

#Kysely jolla saadaan maan vihje jossa matkalaukku sijaitsee ICAO
def query_country_hint(case_location):
    sql_query_country_hint = (f"SELECT hint, name FROM country WHERE iso_country in("
                          f"SELECT iso_country FROM airport WHERE ident = '{case_location}');")
    return sql_query_country_hint

#Vakio kysely joka palauttaa maat, aakkosjärjestyksessä
query_countries = f"SELECT name FROM country WHERE continent = 'EU' ORDER BY name;"


#Kysely jolla saadaan parametri country avulla kyseisen maan lentokenttien ICAOT järjestyksessä large tyypistä alaspäin
def query_country_airports(country):
    sql_query_airports = (f"SELECT ident FROM airport, country "
                      f"WHERE airport.iso_country = country.iso_country and country.name ='{country}'"
                          f" ORDER BY CASE WHEN type = 'large_airport' THEN 1 WHEN type = 'medium_airport' THEN 2 WHEN type = 'small_airport' THEN 3 ELSE 4 END;")
    return sql_query_airports



#Kysely jolla saadaan etäisyys pelaajan ja jonkun toisen paikan välillä, float metreissä!
def query_distance_between_player_locations(playername, icao2):
    sql_query_distance = (f"SELECT ST_Distance_Sphere("
                                    f"ST_GeomFromText(("
                                    f"SELECT CONCAT('POINT (',longitude_deg, ' ',latitude_deg,')') FROM airport WHERE ident in(SELECT location FROM game WHERE id = '{playername}')), 4326), "
                                    f"ST_GeomFromText(("
                                    f"SELECT CONCAT('POINT (',longitude_deg, ' ',latitude_deg,')') FROM airport WHERE ident = '{icao2}'), 4326));")
    return sql_query_distance

#Kysely jolla saadaan etäisyys kahden paikan väliltä metreissä float!
def query_distance_between_locations(icao1, icao2):
    sql_query_distance = (f"SELECT ST_Distance_Sphere("
                                    f"ST_GeomFromText(("
                                    f"SELECT CONCAT('POINT (',longitude_deg, ' ',latitude_deg,')') FROM airport WHERE ident = '{icao1}'), 4326), "
                                    f"ST_GeomFromText(("
                                    f"SELECT CONCAT('POINT (',longitude_deg, ' ',latitude_deg,')') FROM airport WHERE ident = '{icao2}'), 4326));")
    return sql_query_distance


#LOAD KYSELYT ##################

#Kysely jolla kysytään käyttäjän arvot
def query_load_username(username):
    sql_query_load_username = (f"SELECT game.id, game.location, suitcase.location, co2_consumed, total_kilometers, clue_unlocked, travel_count "
                               f"FROM game, suitcase WHERE game.id = suitcase.id and game.id ='{username}';")
    return sql_query_load_username


#INSERT KYSELYT ################ UUDEN PELAAJAN LUOMISEEN

#Kysely jolla päivitetään uusi käyttäjä myös suitcase tauluun
def query_new_suitcase(username):
    sql_query_new_suitcase = (f"INSERT INTO suitcase (id) VALUES ('{username}');")
    return sql_query_new_suitcase

#Kysely jolla päivitetään uusi käyttäjä tietokantaan ja asetetaan alkuarvot
def query_new_username(username):
    sql_query_new_username = (f"INSERT INTO game (id, location, co2_consumed, total_kilometers, clue_unlocked, travel_count, suitcases_found) VALUES ('{username}', 'EFHK', 0, 0, 0, 0, 0);")
    return sql_query_new_username


#CHECK KYSELYT TRUE FALSE ############

#Kysely jolla tarkastetaan löytyykö nimi jo pelin tietokannasta
def query_check_username(username):
    sql_query_check_usernames = (f"SELECT id FROM game WHERE id = '{username}';")
    return sql_query_check_usernames


#FETCH KYSELYT #############

#Kysely jolla saadaan käyttäjän maa LOWERcasena
def query_fetch_user_country(username):
    sql_query_fetch_user_country = (f"SELECT LOWER(name) FROM country WHERE iso_country in("
                                    f"SELECT iso_country FROM airport WHERE ident in("
                                    f"SELECT location FROM game WHERE id = '{username}'));")
    return sql_query_fetch_user_country

#Kysely jolla saadaan käyttäjän matkalaukun maa LOWERcasena
def query_fetch_suitcase_country(username):
    sql_query_fetch_suitcase_country = (f"SELECT LOWER(name) FROM country WHERE iso_country in("
                                        f"SELECT iso_country FROM airport WHERE ident in("
                                        f"SELECT location FROM suitcase WHERE id = '{username}'));")
    return sql_query_fetch_suitcase_country

#Vakio kysely jolla haetaan tietokannasta ihmiset joilla on vähintään yli 1 matkalaukku ja max 5 ihmistä desc order.
sql_query_fetch_leaderboards = (f"SELECT id, suitcases_found FROM game WHERE suitcases_found >= 1 order by suitcases_found desc LIMIT 5;")

#Vakio kysely jolla saadaan olemassaolevat käyttäjät
sql_query_fetch_users = (f"SELECT id FROM game")

#UPDATE KYSELYT #####################

def query_update_suitcase_location(location, username):
    sql_query_update_suitcase_location = (f"UPDATE suitcase SET location = ('{location}') WHERE id = '{username}';")
    return sql_query_update_suitcase_location

#Lisätään pelaajalle kilometrit, co2 määrä, travel count, location tietokantaan talteen
def query_update_player_travel(username, kilometers, count, location):
    sql_query_update_player_travel = (f"UPDATE game SET location = '{location}', total_kilometers = {kilometers}+total_kilometers, co2_consumed = {kilometers*8}+co2_consumed, travel_count = {count}+travel_count WHERE id = '{username}';")
    return sql_query_update_player_travel

#Kysely jolla päivitetään onko pelaaja avannut cluen
def query_update_clue_unlocked(username, int):
    sql_query_update_clue_unlocked = (f"UPDATE game SET clue_unlocked = {int} WHERE id = '{username}';")
    return sql_query_update_clue_unlocked

#Kysely jolla päivitetään peli takaisin alkuun ja lisätään pelaajalle 1 matkalaukku löydetty
def query_reset_game_state(username):
    sql_query_reset_game_state = (f"UPDATE game SET location = 'EFHK', clue_unlocked = 0, total_kilometers = 0, co2_consumed = 0, travel_count = 0, suitcases_found = suitcases_found+1 WHERE id = '{username}';")
    return sql_query_reset_game_state