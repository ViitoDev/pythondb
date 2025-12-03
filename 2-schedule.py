import sqlite3

conection = sqlite3.connect("title.db")
cursor = conection.cursor()
cursor.execute(
    """
        CREATE TABLE films(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            year INTEGER NOT NULL,
            note REAL NOT NULL
        );
    """
)

conection.close()
print("Table was created")