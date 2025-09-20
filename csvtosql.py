import pandas as pd
import mysql.connector

df = pd.read_csv('output.csv')

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="vehicles_db"
)
cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO vehicles (modelName, txdName, gameName, vehicleMakeName, audioNameHash)
        VALUES (%s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()
cursor.close()
conn.close()

print("Inserted Values into Database")
