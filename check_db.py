import sqlite3
import os

db_path = 'recommender.db'
print("Using DB path:", os.path.abspath(db_path))

conn = sqlite3.connect(db_path)
c = conn.cursor()

try:
    c.execute("SELECT COUNT(*) FROM suggestions")
    count = c.fetchone()[0]
    print(f"✅ Total suggestions in database: {count}")
except Exception as e:
    print("❌ Error:", e)

conn.close()
