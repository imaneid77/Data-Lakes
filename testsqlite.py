import sqlite3
# Connexion `a une base de donn´ees (ou cr´eation si elle n'existe pas)
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# Cr´eation d'une table de test
cursor.execute('CREATE TABLE IF NOT EXISTS test_table (id INTEGER PRIMARY KEY, value TEXT)')
cursor.execute('INSERT INTO test_table (value) VALUES ("Hello, SQLite!")')
conn.commit()
# Interrogation de la base
cursor.execute('SELECT * FROM test_table')
print(cursor.fetchall())
conn.close()