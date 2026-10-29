import sqlite3

DB_NAME = "monitoring.db"

def create_database():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS performance(
            id  INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            cpu REAL NOT NULL,
            ram REAL NOT NULL,
            disk REAL NOT NULL,
            network_status TEXT,
            response_time REAL
            
        )    
    """)

def save_performance(
        timestamp, cpu, ram, disk,
        netwrok_status, response_time
):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            INSERT INTO performance (
            timestamp, cpu, ram, disk,
            network_status, response_time
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        timestamp, cpu, ram, disk,
        netwrok_status, response_time
    ))


def get_history(limit=100):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute("""
            SELECT timestamp, cpu, ram, disk,
                    network_status, response_time
            FROM (
                 SELECT *
                 FROM performance
                 ORDER BY id DESC
                 LIMIT ?
            )
            ORDER BY id ASC
        """, (limit,))

        return cursor.fetchall()

if __name__ == "__main__":
    create_database()
    print("Database created succesfully!")