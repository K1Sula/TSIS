import psycopg2
from config import load_config

def insert_users():
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        # Clear the incorrect_phone_numbers table
        cur.execute("TRUNCATE TABLE incorrect_phone_numbers")

        # Получаем от пользователя количество и имена для вставки
        num_users = int(input("Enter the number of users to insert: "))
        for i in range(num_users):
            first_name = input(f"Enter the first name of user {i+1}: ")
            last_name = input(f"Enter the last name of user {i+1}: ")
            phone_number = input(f"Enter the phone number of user {i+1}: ")
            email = input(f"Enter the email of user {i+1}: ")
            address = input(f"Enter the address of user {i+1}: ")

            # Insert user data into the contacts table
            cur.execute("""
                INSERT INTO contacts (first_name, last_name, phone_number, email, address)
                VALUES (%s, %s, %s, %s, %s)
            """, (first_name, last_name, phone_number, email, address))

        print("All users inserted successfully.")

        conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error inserting users:", error)
        conn.rollback()  # Rollback the transaction in case of error
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    insert_users()
