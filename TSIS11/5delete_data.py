import psycopg2
from config import load_config

def delete_contact():
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        # Ask the user for the deletion method
        deletion_method = input("Enter '1' to delete by username or '2' to delete by phone number: ")

        if deletion_method == '1':
            username = input("Enter the username to delete: ")
            query = "DELETE FROM contacts WHERE first_name = %s"
            cur.execute(query, (username,))
            print("Data deleted successfully for contacts with username:", username)
        elif deletion_method == '2':
            phone_number = input("Enter the phone number to delete: ")
            query = "DELETE FROM contacts WHERE phone_number = %s"
            cur.execute(query, (phone_number,))
            print("Data deleted successfully for contacts with phone number:", phone_number)
        else:
            print("Invalid deletion method. Please enter '1' or '2'.")

        conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error deleting contacts:", error)
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    delete_contact()