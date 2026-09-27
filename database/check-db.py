import os
import sqlite3

alias_path = "/etc/adachi-alias/alias.db"

if not os.path.exists(alias_path):
    print("Alias Database not found. Creating it for you")
    conn = sqlite3.connect(alias_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS alias (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        alias TEXT NOT NULL,
                        script_path TEXT NOT NULL
                    )''')
    conn.commit()
    conn.close()
else:
    exit(0)