from connect import connect
import csv

# CREATE TABLE
def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) NOT NULL,
            phone VARCHAR(20) UNIQUE NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()


# INSERT (console)
def insert_contact():
    username = input("Name: ")
    phone = input("Phone: ")

    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
            (username, phone)
        )
        conn.commit()
        print("Added!")
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()


# INSERT FROM CSV
def insert_from_csv():
    conn = connect()
    cur = conn.cursor()

    with open("contacts.csv", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                cur.execute(
                    "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
                    (row[0], row[1])
                )
            except:
                print("Skipped:", row)

    conn.commit()
    cur.close()
    conn.close()


# SELECT (search)
def search():
    keyword = input("Search name: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM phonebook WHERE username ILIKE %s",
        (f"%{keyword}%",)
    )

    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No results found.")

    cur.close()
    conn.close()


# SELECT ALL
def show_all():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("Phonebook is empty.")

    cur.close()
    conn.close()


# UPDATE (by name + phone)
def update():
    username = input("Enter username: ")
    phone = input("Enter current phone: ")
    new_phone = input("New phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE phonebook SET phone=%s WHERE username=%s AND phone=%s",
        (new_phone, username, phone)
    )
    conn.commit()

    print("Updated!")

    cur.close()
    conn.close()


# DELETE (by name + phone)
def delete():
    username = input("Enter username: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM phonebook WHERE username=%s AND phone=%s",
        (username, phone)
    )
    conn.commit()

    print("Deleted!")

    cur.close()
    conn.close()


# MENU
def menu():
    create_table()

    while True:
        print("\n1.Add 2.Search 3.Update 4.Delete 5.CSV 6.ShowAll 0.Exit")
        choice = input(">>> ")

        if choice == "1":
            insert_contact()
        elif choice == "2":
            search()
        elif choice == "3":
            update()
        elif choice == "4":
            delete()
        elif choice == "5":
            insert_from_csv()
        elif choice == "6":
            show_all()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")


# START PROGRAM
if __name__ == "__main__":
    menu()