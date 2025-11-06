import sqlite3

DB_PATH = 'data_store/pyano.db'

# SQL naredba za brisanje retka
sql_delete_one = '''
    DELETE FROM piano
    WHERE id = ?
'''

# Podaci: (ID_retka_koji_brisemo,)
# Mora biti tuple, pa stavljamo zarez (,) na kraju ako ima samo jedan element
id_za_brisanje = (5,)  # Npr. brišemo redak s ID-om 5

try:
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        
        # Izvršavanje DELETE naredbe
        cursor.execute(sql_delete_one, id_za_brisanje)
        
        # OBAVEZNO: Potvrda (commit) promjena za spremanje
        conn.commit()
        
        # Opcionalna provjera je li redak stvarno obrisan
        if cursor.rowcount > 0:
            print(f'Uspješno obrisan redak (ID: {id_za_brisanje[0]}).')
        else:
            print(f'Nijedan redak nije obrisan. ID {id_za_brisanje[0]} možda ne postoji.')

except Exception as ex:
    print(f'Dogodila se greska kod DELETE-a: {ex}!')