import sqlite3

DB_PATH = 'data_store/pyano.db'

# SQL naredba za ažuriranje (promjenu) podataka
sql_update_one = '''
    UPDATE piano
    SET brand = ?, model = ? 
    WHERE id = ?
'''

# Podaci: (nova_vrijednost_branda, nova_vrijednost_modela, ID_retka_koji_mijenjamo)
podaci_za_update = ('Korg', 'Minilogue', 3)  # Npr. mijenjamo redak s ID-om 3

try:
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        
        # Izvršavanje UPDATE naredbe
        cursor.execute(sql_update_one, podaci_za_update)
        
        # OBAVEZNO: Potvrda (commit) promjena za spremanje
        conn.commit()
        
        # Opcionalna provjera je li redak stvarno ažuriran
        if cursor.rowcount > 0:
            print(f'Uspješno ažuriran redak (ID: {podaci_za_update[2]}).')
        else:
            print(f'Nijedan redak nije ažuriran. ID {podaci_za_update[2]} možda ne postoji.')

except Exception as ex:
    print(f'Dogodila se greska kod UPDATE-a: {ex}!')