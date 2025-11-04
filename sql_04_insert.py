import sqlite3


DB_PATH = 'data_store/pyano.db'
sql_insert_into_table = '''
    INSERT INTO piano(name, price, year_of_production)
    VALUES(?, ?, ?)
'''


while True:
    piano_name = input('Upisite naziv piana: ')
    piano_price = float(input('Upisite cijenu piana: '))
    piano_yop = int(input('Upisite godinu proizvodnje piana: '))

    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            # !!! Ako u paramterima imate samo jednu vrijednost,
            # onda je pisete sa zarezom iza. Primjer: (value1,) | KRIVO (value1)
            cursor.execute(sql_insert_into_table, (piano_name, piano_price, piano_yop))

    except Exception as ex:
        print(f'Dogodila se greska {ex}!')

    next_piano = input('Unos novog piana? (Da/Ne): ')
    if next_piano.lower() != 'da':
        break
