from connect import connect
import json
import csv

# ---------------- ADD CONTACT ----------------
def add_contact():
    name = input("Name: ")
    email = input("Email: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL upsert_contact(%s,%s)", (name, email))
    conn.commit()
    conn.close()

# ---------------- ADD PHONE ----------------
def add_phone():
    name = input("Name: ")
    phone = input("Phone: ")
    ptype = input("Type (home/work/mobile): ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL add_phone(%s,%s,%s)", (name, phone, ptype))
    conn.commit()
    conn.close()

# ---------------- MOVE GROUP ----------------
def move_group():
    name = input("Name: ")
    group = input("Group: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL move_to_group(%s,%s)", (name, group))
    conn.commit()
    conn.close()

# ---------------- SEARCH ----------------
def search():
    q = input("Search: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s)", (q,))
    for row in cur.fetchall():
        print(row)

    conn.close()

# ---------------- FILTER ----------------
def filter_group():
    group = input("Group: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.username, g.name
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name=%s
    """, (group,))

    for row in cur.fetchall():
        print(row)

    conn.close()

# ---------------- SORT ----------------
def sort_contacts():
    field = input("Sort by (name/birthday/date): ")

    mapping = {
        "name": "username",
        "birthday": "birthday",
        "date": "created_at"
    }

    conn = connect()
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM contacts ORDER BY {mapping[field]}")
    for row in cur.fetchall():
        print(row)

    conn.close()

# ---------------- PAGINATION ----------------
def paginate():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_contacts_page(%s,%s)", (limit, offset))

    for row in cur.fetchall():
        print(row)

    conn.close()

# ---------------- EXPORT JSON ----------------
def export_json():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.username, c.email, p.phone, p.type
        FROM contacts c
        LEFT JOIN phones p ON c.id = p.contact_id
    """)

    data = cur.fetchall()

    with open("contacts.json", "w") as f:
        json.dump(data, f, default=str)

    conn.close()
    print("Exported!")

# ---------------- IMPORT JSON ----------------
def import_json():
    with open("contacts.json") as f:
        data = json.load(f)

    conn = connect()
    cur = conn.cursor()

    for row in data:
        name = row[0]

        cur.execute("SELECT id FROM contacts WHERE username=%s", (name,))
        exists = cur.fetchone()

        if exists:
            choice = input(f"{name} exists (skip/overwrite): ")
            if choice != "overwrite":
                continue
            cur.execute("DELETE FROM contacts WHERE username=%s", (name,))

        cur.execute("INSERT INTO contacts(username,email) VALUES(%s,%s)", (row[0], row[1]))

    conn.commit()
    conn.close()

# ---------------- MENU ----------------
def menu():
    while True:
        print("\n1.Add 2.AddPhone 3.MoveGroup 4.Search 5.Filter 6.Sort 7.Page 8.Export 9.Import 0.Exit")
        c = input(">>> ")

        if c == "1":
            add_contact()
        elif c == "2":
            add_phone()
        elif c == "3":
            move_group()
        elif c == "4":
            search()
        elif c == "5":
            filter_group()
        elif c == "6":
            sort_contacts()
        elif c == "7":
            paginate()
        elif c == "8":
            export_json()
        elif c == "9":
            import_json()
        elif c == "0":
            break

if __name__ == "__main__":
    menu()