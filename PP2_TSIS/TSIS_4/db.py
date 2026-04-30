import psycopg2

DB_CONFIG = {
    "dbname": "snake_db",
    "user": "postgres",
    "password": "052007",
    "host": "localhost",
    "port": "5432"
}

def leaderboard():
    c = conn()
    cur = c.cursor()

    cur.execute("""
        SELECT players.username, sessions.score, sessions.level
        FROM sessions
        JOIN players ON players.id = sessions.player_id
        ORDER BY sessions.score DESC
        LIMIT 10
    """)

    data = cur.fetchall()
    c.close()
    return data

def conn():
    return psycopg2.connect(**DB_CONFIG)

def init():
    c = conn()
    cur = c.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS players(
        id SERIAL PRIMARY KEY,
        username TEXT UNIQUE
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS sessions(
        id SERIAL PRIMARY KEY,
        player_id INT,
        score INT,
        level INT
    )
    """)

    c.commit()
    c.close()

def get_player(name):
    c = conn()
    cur = c.cursor()

    cur.execute("SELECT id FROM players WHERE username=%s", (name,))
    r = cur.fetchone()

    if r:
        return r[0]

    cur.execute("INSERT INTO players(username) VALUES(%s) RETURNING id", (name,))
    pid = cur.fetchone()[0]

    c.commit()
    c.close()
    return pid

def save_score(pid, score, level):
    c = conn()
    cur = c.cursor()

    cur.execute(
        "INSERT INTO sessions(player_id,score,level) VALUES(%s,%s,%s)",
        (pid, score, level)
    )

    c.commit()
    c.close()