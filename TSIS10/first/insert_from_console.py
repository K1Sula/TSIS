import psycopg2
from config import load_config

def insert_from_console():
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        phone_number = input("Enter Phone Number: ")
        email = input("Enter Email Address: ")
        address = input("Enter Address: ")

        cur.execute("""
            INSERT INTO contacts (first_name, last_name, phone_number, email, address)
            VALUES (%s, %s, %s, %s, %s)
        """, (first_name, last_name, phone_number, email, address))

        conn.commit()
        print("Data inserted successfully from console.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    insert_from_console()
