import psycopg2

conn = psycopg2.connect(
    dbname="snake_db",
    user="postgres",
    password="052007",
    host="localhost",
    port="5432"
)

print("DB CONNECTED")