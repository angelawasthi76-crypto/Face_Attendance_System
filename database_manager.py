import sqlite3

conn = sqlite3.connect("database/attendance.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
date TEXT,
entry_time TEXT,
exit_time TEXT,
duration TEXT
)
""")

conn.commit()


def mark_entry(name, date, time):

    cursor.execute("""
    SELECT * FROM attendance
    WHERE name=? AND date=?
    """, (name, date))

    row = cursor.fetchone()

    if row is None:

        cursor.execute("""
        INSERT INTO attendance(name,date,entry_time)
        VALUES(?,?,?)
        """, (name, date, time))

        conn.commit()


def mark_exit(name, date, time):

    cursor.execute("""
    UPDATE attendance
    SET exit_time=?
    WHERE name=? AND date=?
    """, (time, name, date))

    conn.commit()


def update_duration(name, date, duration):

    cursor.execute("""
    UPDATE attendance
    SET duration=?
    WHERE name=? AND date=?
    """, (duration, name, date))

    conn.commit()