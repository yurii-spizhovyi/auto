import psycopg2

connection = psycopg2.connect(
    user='admin',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='hw26'
)
cursor = connection.cursor()
a = cursor.execute("SELECT * FROM students")
print(f"Fetch all: {cursor.fetchall()}")
#print(f"Fetch one: {cursor.fetchone()}")
b =0
#print(a)
c = 0