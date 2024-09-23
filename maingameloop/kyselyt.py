


#Kysely jolla saadaan maan vihje jossa matkalaukku sijaitsee ICAO
def query_country_hint(case_location):
    sql_query_country_hint = (f"SELECT hint FROM country WHERE iso_country like("
                          f"SELECT iso_country FROM airport WHERE ident = '{case_location}');")
    return sql_query_country_hint