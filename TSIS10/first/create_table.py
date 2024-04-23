import psycopg2
from config import load_config

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE contacts (
            contact_id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100),
            phone_number VARCHAR(20) NOT NULL,
            email VARCHAR(255),
            address VARCHAR(255)
        )
        """,
        """
        CREATE TABLE groups (
            group_id SERIAL PRIMARY KEY,
            group_name VARCHAR(100) NOT NULL
        )
        """,
        """
        CREATE TABLE contact_groups (
            contact_id INTEGER NOT NULL,
            group_id INTEGER NOT NULL,
            PRIMARY KEY (contact_id, group_id),
            FOREIGN KEY (contact_id) REFERENCES contacts (contact_id) ON DELETE CASCADE,
            FOREIGN KEY (group_id) REFERENCES groups (group_id) ON DELETE CASCADE
        )
        """
    )
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()
