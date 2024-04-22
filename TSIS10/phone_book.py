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

# Main function
def main():
    conn = connect()
    if conn:
        create_phonebook_table(conn)

        # Insert data from CSV file
        insert_from_csv(conn, "phonebook_data.csv")

        # Insert data from console
        insert_from_console(conn)

        # Update data
        update_data(conn, "John Doe", new_name="Jane Doe")

        # Query data
        print("All entries:")
        all_entries = query_data(conn)
        for entry in all_entries:
            print(entry)

        print("Query by name:")
        name_query = query_data(conn, filter_name="Jane Doe")
        print(name_query)

        # Delete data
        delete_data(conn, filter_name="Jane Doe")

        conn.close()
    else:
        print("Connection to PostgreSQL failed.")

if __name__ == "__main__":
    main()
