import psycopg2
from config import load_config

def update_contact():
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        # Ask user for contact ID
        contact_id = input("Input contact ID to update: ")

        # Ask user for new first name
        new_first_name = input("Input new first name (leave empty to skip): ")

        # Ask user for new last name
        new_last_name = input("Input new last name (leave empty to skip): ")

        # Ask user for new phone number
        new_phone_number = input("Input new phone number (leave empty to skip): ")

        # Ask user for new email
        new_email = input("Input new email (leave empty to skip): ")

        # Ask user for new address
        new_address = input("Input new address (leave empty to skip): ")

        # Construct the UPDATE query
        update_query = "UPDATE contacts SET "
        update_values = []

        # Check if new first name is provided
        if new_first_name:
            update_query += "first_name = %s, "
            update_values.append(new_first_name)

        # Check if new last name is provided
        if new_last_name:
            update_query += "last_name = %s, "
            update_values.append(new_last_name)

        # Check if new phone number is provided
        if new_phone_number:
            update_query += "phone_number = %s, "
            update_values.append(new_phone_number)

        # Check if new email is provided
        if new_email:
            update_query += "email = %s, "
            update_values.append(new_email)

        # Check if new address is provided
        if new_address:
            update_query += "address = %s, "
            update_values.append(new_address)

        # Remove the trailing comma and space
        update_query = update_query.rstrip(", ")

        # Add the WHERE clause for the specific contact_id
        update_query += " WHERE contact_id = %s"

        # Append the contact_id to the update values
        update_values.append(contact_id)

        # Execute the UPDATE query
        cur.execute(update_query, update_values)

        conn.commit()
        print("Data updated successfully.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    update_contact()