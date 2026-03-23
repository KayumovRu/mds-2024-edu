import sqlite3

DB_PATH = "backend/experiments.db"

def init_db():
   conn = sqlite3.connect(DB_PATH)
   cursor = conn.cursor()

   cursor.execute("""
   CREATE TABLE IF NOT EXISTS experiments (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       model_name TEXT,
       train_size REAL,
       max_iter INTEGER,
       score REAL,
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   )
   """)

   conn.commit()
   conn.close()

def save_experiment(model_name, train_size, max_iter, score):
   conn = sqlite3.connect(DB_PATH)
   cursor = conn.cursor()

   cursor.execute("""
   INSERT INTO experiments (model_name, train_size, max_iter, score)
   VALUES (?, ?, ?, ?)
   """, (model_name, train_size, max_iter, score))

   conn.commit()
   conn.close()

