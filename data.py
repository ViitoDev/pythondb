import sqlite3

def connect_db():
    connection = sqlite3.connect("title.db")
    return connection

def insert_data(name, year, note):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute(
    """
        INSERT INTO films(name, year, note)
        VALUES (?, ?, ?)
    """, (name, year, note)
    )
    connection.commit()
    connection.close()

def data_obtain():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM films")
    data = cursor.fetchall()
    cursor.close()
    return data