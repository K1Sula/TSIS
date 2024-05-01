import psycopg2
from config import load_config

def get_contacts_by_name(first_name, limit, offset):
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        query = "SELECT * FROM contacts WHERE first_name = %s LIMIT %s OFFSET %s"
        cur.execute(query, (first_name, limit, offset))
        
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

def get_contacts_by_phone(phone_number, limit, offset):
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        query = "SELECT * FROM contacts WHERE phone_number = %s LIMIT %s OFFSET %s"
        cur.execute(query, (phone_number, limit, offset))
        
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
            
name_found = input("Enter name that you need: ")
number_found = input("Enter number that you need: ")
limit = int(input("Enter limit: "))
offset = int(input("Enter offset: "))

if __name__ == '__main__':
    # Example usage: get contacts with a specific first name
    contacts_with_name = get_contacts_by_name(name_found, limit, offset)
    if contacts_with_name:
        print(f"Contacts with name {name_found}:", contacts_with_name)
    else:
        print(f"No contacts found with name {name_found}.")

    # Example usage: get contacts with a specific phone number
    contacts_with_phone = get_contacts_by_phone(number_found, limit, offset)
    if contacts_with_phone:
        print(f"Contacts with phone number {number_found} :", contacts_with_phone)
    else:
        print(f"No contacts found with phone number {number_found}.")


"""
sultankadyr@Air-Sultan TSIS11 % python3 queying.py
Enter name that you need: Sultan 
Enter number that you need: 8771061393
Enter limit: 0
Enter offset: 1
No contacts found with name Sultan .
No contacts found with phone number 8771061393.
sultankadyr@Air-Sultan TSIS11 % python3 queying.py
Enter name that you need: Sultan
Enter number that you need: 87714061393
Enter limit: 1
Enter offset: 1
Contacts with name Sultan: [(2, 'Sultan', 'KAbi', '87714061393', 'sultankadyr77@gmail.com', 'zhetisy 4')]
Contacts with phone number 87714061393 : [(2, 'Sultan', 'KAbi', '87714061393', 'sultankadyr77@gmail.com', 'zhetisy 4')]
sultankadyr@Air-Sultan TSIS11 % python3 queying.py
Enter name that you need: Sultan
Enter number that you need: 87714061393
Enter limit: 2
Enter offset: 0
Contacts with name Sultan: [(1, 'Sultan', 'Kadyr', '87714061393', 'sssultan.k@gmail.com', 'zhetisy4'), (2, 'Sultan', 'KAbi', '87714061393', 'sultankadyr77@gmail.com', 'zhetisy 4')]
Contacts with phone number 87714061393 : [(1, 'Sultan', 'Kadyr', '87714061393', 'sssultan.k@gmail.com', 'zhetisy4'), (2, 'Sultan', 'KAbi', '87714061393', 'sultankadyr77@gmail.com', 'zhetisy 4')]
"""

# Пример с лимитом и без оффсета:

# Если мы используем только лимит, то мы просто ограничиваем количество записей, которые будут возвращены.
# Например, если у нас есть 15 имен, и мы используем лимит 5, то будет возвращено только первые 5 имен.

# Пример с оффсетом и лимитом:

# Теперь добавим оффсет, чтобы начать выборку с определенной позиции.
# Если мы хотим показать вторую страницу, нам нужно сначала пропустить первые 5 записей (так как на первой странице уже отображены), а затем взять следующие 5 записей.
# Для этого используется комбинация лимита и оффсета.