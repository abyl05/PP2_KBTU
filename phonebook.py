from connect import connect

# ------------------------
# INSERT / UPDATE (UPSERT)
# ------------------------
def upsert_user():
    username = input("Name: ")
    phone = input("Phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL upsert_user(%s, %s)", (username, phone))
    conn.commit()

    print("Inserted or Updated!")

    cur.close()
    conn.close()


# ------------------------
# SEARCH (FUNCTION)
# ------------------------
def search():
    keyword = input("Search: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_pattern(%s)", (keyword,))
    rows = cur.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No results.")

    cur.close()
    conn.close()


# ------------------------
# PAGINATION
# ------------------------
def show_paginated():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM get_contacts_paginated(%s, %s)",
        (limit, offset)
    )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


# ------------------------
# DELETE (PROCEDURE)
# ------------------------
def delete():
    username = input("Enter username (or leave empty): ")
    phone = input("Enter phone (or leave empty): ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL delete_user(%s, %s)", (username, phone))
    conn.commit()

    print("Deleted!")

    cur.close()
    conn.close()


# ------------------------
# BULK INSERT (ARRAY)
# ------------------------
def insert_many():
    names = input("Enter names (comma separated): ").split(",")
    phones = input("Enter phones (comma separated): ").split(",")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "CALL insert_many(%s, %s)",
        (names, phones)
    )
    conn.commit()

    print("Bulk insert done!")

    cur.close()
    conn.close()


# ------------------------
# MENU
# ------------------------
def menu():
    while True:
        print("\n1.Upsert 2.Search 3.Pagination 4.Delete 5.BulkInsert 0.Exit")
        choice = input(">>> ")

        if choice == "1":
            upsert_user()
        elif choice == "2":
            search()
        elif choice == "3":
            show_paginated()
        elif choice == "4":
            delete()
        elif choice == "5":
            insert_many()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")


# ------------------------
# START
# ------------------------
if __name__ == "__main__":
    menu()