


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



#Kysely joka palauttaa käyttäjän etäisyyden matkalaukkuun METREINÄ!
def query_distance_from_goal(case_location, game_id):
    sql_query_distance_from_goal = (f"SELECT ST_Distance_Sphere("
                                    f"ST_GeomFromText(("
                                    f"SELECT CONCAT('POINT (',longitude_deg, ' ',latitude_deg,')') FROM airport WHERE ident in(SELECT location FROM game WHERE id = {game_id}))), "
                                    f"ST_GeomFromText(("
                                    f"SELECT CONCAT('POINT (',longitude_deg, ' ',latitude_deg,')') from Airport Where ident = '{case_location}')));")
    return sql_query_distance_from_goal

