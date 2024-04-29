import psycopg2
import csv

# Function to connect to PostgreSQL
def connect():
    try:
        conn = psycopg2.connect(
            dbname="dika",
            user="dika",
            password="dikamiko2006",
            host="localhost",
            port="3000"
        )
        return conn
    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL:", e)

# Function to create PhoneBook table
def create_phonebook_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS phonebook (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                phone VARCHAR(20)
            )
        """)
        conn.commit()
        cursor.close()
        print("PhoneBook table created successfully.")
    except psycopg2.Error as e:
        print("Error creating PhoneBook table:", e)

# Function to insert data from CSV file
def insert_from_csv(conn, filename):
    try:
        cursor = conn.cursor()
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                cursor.execute("""
                    INSERT INTO phonebook (name, phone) 
                    VALUES (%s, %s)
                """, (row[0], row[1]))
            conn.commit()
        cursor.close()
        print("Data inserted from CSV successfully.")
    except psycopg2.Error as e:
        print("Error inserting data from CSV:", e)

# Function to insert data from console
def insert_from_console(conn):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO phonebook (name, phone) 
            VALUES (%s, %s)
        """, (name, phone))
        conn.commit()
        cursor.close()
        print("Data inserted from console successfully.")
    except psycopg2.Error as e:
        print("Error inserting data from console:", e)

# Function to update data in the table
def update_data(conn, name, new_name=None, new_phone=None):
    try:
        cursor = conn.cursor()
        if new_name:
            cursor.execute("""
                UPDATE phonebook 
                SET name = %s 
                WHERE name = %s
            """, (new_name, name))
        if new_phone:
            cursor.execute("""
                UPDATE phonebook 
                SET phone = %s 
                WHERE name = %s
            """, (new_phone, name))
        conn.commit()
        cursor.close()
        print("Data updated successfully.")
    except psycopg2.Error as e:
        print("Error updating data:", e)

# Function to query data from the table
def query_data(conn, filter_name=None):
    try:
        cursor = conn.cursor()
        if filter_name:
            cursor.execute("""
                SELECT * FROM phonebook 
                WHERE name = %s
            """, (filter_name,))
        else:
            cursor.execute("SELECT * FROM phonebook")
        rows = cursor.fetchall()
        cursor.close()
        return rows
    except psycopg2.Error as e:
        print("Error querying data:", e)

# Function to delete data from the table
def delete_data(conn, filter_name=None, filter_phone=None):
    try:
        cursor = conn.cursor()
        if filter_name:
            cursor.execute("""
                DELETE FROM phonebook 
                WHERE name = %s
            """, (filter_name,))
        elif filter_phone:
            cursor.execute("""
                DELETE FROM phonebook 
                WHERE phone = %s
            """, (filter_phone,))
        conn.commit()
        cursor.close()
        print("Data deleted successfully.")
    except psycopg2.Error as e:
        print("Error deleting data:", e)

# Function to call search_phonebook function
def search_phonebook(conn, pattern):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
        rows = cursor.fetchall()
        cursor.close()
        return rows
    except psycopg2.Error as e:
        print("Error searching phonebook:", e)

# Procedure to call insert_or_update_user procedure
def insert_or_update_user(conn, name, phone):
    try:
        cursor = conn.cursor()
        cursor.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
        conn.commit()
        cursor.close()
        print("User inserted/updated successfully.")
    except psycopg2.Error as e:
        print("Error inserting/updating user:", e)

# Procedure to call insert_many_users procedure
def insert_many_users(conn, names, phones):
    try:
        cursor = conn.cursor()
        cursor.callproc("insert_many_users", (names, phones))
        invalid_data = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        if invalid_data:
            print("Invalid data:", invalid_data)
        else:
            print("All users inserted successfully.")
    except psycopg2.Error as e:
        print("Error inserting users:", e)

# Function to call get_phonebook_page function
def get_phonebook_page(conn, limit, offset):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM get_phonebook_page(%s, %s)", (limit, offset))
        rows = cursor.fetchall()
        cursor.close()
        return rows
    except psycopg2.Error as e:
        print("Error getting phonebook page:", e)

# Procedure to call delete_user procedure
def delete_user(conn, username=None, phone=None):
    try:
        cursor = conn.cursor()
        cursor.callproc("delete_user", (username, phone))
        conn.commit()
        cursor.close()
        print("User(s) deleted successfully.")
    except psycopg2.Error as e:
        print("Error deleting user(s):", e)

# Main function
def main():
    conn = connect()
    if conn:
        create_phonebook_table(conn)

        # # Search phonebook
        # print("Search results:")
        # search_results = search_phonebook(conn, "John")
        # for result in search_results:
        #     print(result)

        # Insert or update user
        insert_or_update_user(conn, "John Doe", "1234567890")

        # Insert many users
        insert_many_users(conn, ["Jane Doe", "Alice", "Bob"], ["9876543210", "123456", "6543219870"])

        # Query phonebook page
        print("Phonebook page:")
        phonebook_page = get_phonebook_page(conn, 2, 0)
        for entry in phonebook_page:
            print(entry)

        # Delete user
        delete_user(conn, username="John Doe")

        conn.close()
    else:
        print("Connection to PostgreSQL failed.")

if __name__ == "__main__":
    main()
