

sql_query_airport_name = f"SELECT name FROM airport WHERE iso_country = 'FI'"
sql_query_airport_elevation = f"SELECT elevation_ft FROM airport WHERE ident = 'EFHK'"



sql_query_country_hint = (f"SELECT hint FROM country WHERE iso_country like("
                          f"SELECT iso_country FROM airport WHERE ident = '{waldogame.case_location}');")