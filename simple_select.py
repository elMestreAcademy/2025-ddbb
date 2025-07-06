import mysql.connector

conn = mysql.connector.connect(
            host= "localhost",
            user= "root",
            password= "krono",
            database= "world"
)

cursor = conn.cursor()

cursor.execute("""
    SELECT *
    FROM `city`
    ORDER BY `Population` DESC
""")

resultados = cursor.fetchall()
conn.close()

for row in resultados:
   print(row)
