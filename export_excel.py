import sqlite3
import pandas as pd
from datetime import datetime
import os

# Connect to database
conn = sqlite3.connect("database/attendance.db")

# Read attendance table
query = """
SELECT name, date, entry_time, exit_time, duration
FROM attendance
"""

df = pd.read_sql_query(query, conn)

conn.close()

# Create reports folder if it doesn't exist
os.makedirs("reports", exist_ok=True)

# Today's date
today = datetime.now().strftime("%Y-%m-%d")

# Excel file name
filename = f"reports/attendance_{today}.xlsx"

# Save to Excel
df.to_excel(filename, index=False)

print("Excel report created successfully!")
print("Saved as:", filename)