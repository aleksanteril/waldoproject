def query_country_airports(country):
    query_airports = (f"SELECT ident FROM airport, country "
                      f"WHERE airport.iso_country = country.iso_country and country.name ='{country}';")
    country = input("")
