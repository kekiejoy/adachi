import os
import sqlite3
import sys


parent_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)
sys.path.append(parent_dir)

from checkroot import check_root


alias_path = "/etc/adachi-alias/alias.db"

if not os.path.exists(alias_path):
    print("Alias Database not found. Creating it for you")
    check_root()
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