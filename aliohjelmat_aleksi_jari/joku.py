#OHJELMA:
#STEP 1 = PELINALUSTUS
# - PRINT PELIOHJEET
# - PRINT KÄYTTÄJÄLLE OHJEET & KOMENTOVAIHTOEHDOT
# - MÄÄRITÄ SIJAINTI
# - ARVO MARKALAUKUN SIJAINTI
# - ALOITA VIHJE LASKURI            nämä täytyy alustaa funktion ulkopuolella koska muuttuja sokeus!
# - ALOITA PÄÄSTÖ LASKURI
# - KYSY NIMI
# - KYSY SEURAAVA MATKUSTUSMAA   #Komento()
# - MATKUSTA                   #Matkustus()

# STEP 2
# - ILMOITA SAAPUMISMAAN TIEDOT
# - PÄIVITÄ SIJAINTI MATKALAUKKUUN
# - ILMOITA PELAAJALLE = Kylmempää/lämpimämpää
# - KM LASKURIN PÄIVITTYMINEN
# - VIHJE LASKURIN PÄIVITTYMINEN
# - KYSY PELAAJALTA UUSI MATKUSTUSMAA

# STEP 3
# - Luo kirjasto jossa vain sallitut matkustusmaat (eurooppa)            #Rajataan SQL kyselyn avulla nämä
# - Pelaaja saapuu automaattisesti syöttämänsä maan päälentokentälle #Pelaaja voisi saapua aina lentokentälle mikä tulee 1. maan listalla vaikkapa order by name asc
                                                                    #Tämä koska kaikissa maissa ei ole large_airport

#import random

#  PELINALUSTUS
def aloita_peli():
    print("PRINT TAUSTATARINA TJPS")
    print("PRINT TARKOITUS esim. Löydä matkalaukku niin ja näin.")
    print("PRINT OHJEISTUS MITEN MATKUSTAA / SIIRTYY / komennot")
    print("PRINT KIRJOITA sana ICAO -> Kirjoita maan -> saat vastauksena sen pääkentän ICAO:n ")


    pelaaja = input("SYÖTÄ PELAAJAN NIMI: ")
    current_location = "EFHK" #Tämä täytyisi insertata tietokantaan game.location
    print (f"Olet lentokentälklä: {current_location}")
    matkalaukun_sijainti = random_sijainti() # ARPOO LAUKUN SIJAINNIN
    # MÄÄRITETÄÄN KM LASKURI JA VIHJE LASKURI
    #Tähän asti näyttää hyvältä. loput jutut voisi hajauttaa ja tehdä funktiot itsenäisiksi osiksi
    #ehkä jopa omiin .py fileihin ettei tule
    #Liian spagettimainen koodi

    total_kilometrit = 0
    vihje_counter = 0


    #Miks tää on pelinalustus funktion sisällä??
    #Komento funktiosta ois hyvä saada erillinen mikä palauttaa sen käyttäjän inputin sit parametrina siis
    while True:
        user_input = input("Syötä seuraavan kentän ICAO tai kirjoita ICAO:").upper()

        if user_input == "ICAO":
            country_name = input("Syötä maan nimi: ")
            icao_lista(country_name)
        else:
            if len(user_input) == 4:
                print(f"Matkustat lentokentälle {user_input}...")
                current_location = user_input
            else:
                print("Virheellinen koodi")

def random_sijainti():
    return "Placeholder"

def icao_lista(country_name):
    sql = (
        "SELECT airport.ident AS icao_code "
        "FROM airport "
        "JOIN country ON airport.iso_country = country.iso_country "
        "WHERE country.name = '" + country_name + "' AND airport.type = 'large_airport';"
    )
    cursor = yhteys.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()

    if results:
        print(f"Suuret lentokentät maassa {country_name}:")
        for result in results:
            print(f"- ICAO-koodi: {result[0]}")
    else:
         print(f"Ei löytynyt suuria lentokenttiä maassa: {country_name}")

aloita_peli()