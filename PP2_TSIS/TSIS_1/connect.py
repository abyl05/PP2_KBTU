import psycopg2

def get_conn():
    return psycopg2.connect(
        dbname="phonebook",   # 👈 имя БД
        user="postgres",      # 👈 твой пользователь
        password="052007",  # 👈 пароль (или свой)
        host="localhost",
        port="5432"
    )