import psycopg2
from config import load_config

def get_contacts_by_name(first_name):
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        query = "SELECT * FROM contacts WHERE first_name = %s"
        cur.execute(query, (first_name,))
        
        contacts = cur.fetchall()
        
        return contacts
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error fetching contacts by name:", error)
        return None
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def get_contacts_by_phone(phone_number):
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        query = "SELECT * FROM contacts WHERE phone_number = %s"
        cur.execute(query, (phone_number,))
        
        contacts = cur.fetchall()
        
        return contacts
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error fetching contacts by phone number:", error)
        return None
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
            
name_found = str(input("Enter name that you need: "))
number_found = str(input("Enter number that you need: "))

if __name__ == '__main__':
    # Example usage: get contacts with a specific first name
    contacts_with_name = get_contacts_by_name(name_found )
    if contacts_with_name:
        print(f"Contacts with name {name_found}:", contacts_with_name)
    else:
        print(f"No contacts found with name {name_found}.")

    # Example usage: get contacts with a specific phone number
    contacts_with_phone = get_contacts_by_phone(number_found )
    if contacts_with_phone:
        print(f"Contacts with phone number {number_found} :", contacts_with_phone)
    else:
        print(f"No contacts found with phone number {number_found}.")
