import psycopg2
from config import load_config

def create_tables():
    """ Create tables, function, temporary table, and procedure in the PostgreSQL database"""
    commands = (
        """
        CREATE SEQUENCE IF NOT EXISTS contacts_seq;
        CREATE TABLE IF NOT EXISTS contacts (
            contact_id BIGINT PRIMARY KEY DEFAULT nextval('contacts_seq'),
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100),
            phone_number VARCHAR(20) NOT NULL,
            email VARCHAR(255),
            address VARCHAR(255)
        )
        """,
        """
        DROP FUNCTION IF EXISTS search_records(pattern TEXT);
        CREATE OR REPLACE FUNCTION search_records(pattern TEXT) RETURNS TABLE (
            id BIGINT,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            phone_number VARCHAR(20),
            email VARCHAR(255),
            address VARCHAR(255)
        ) AS $$
        BEGIN
            RETURN QUERY 
            SELECT * FROM contacts 
            WHERE 
                contacts.first_name ILIKE '%' || pattern || '%' OR
                contacts.last_name ILIKE '%' || pattern || '%' OR
                contacts.phone_number ILIKE '%' || pattern || '%' OR
                contacts.email ILIKE '%' || pattern || '%' OR
                contacts.address ILIKE '%' || pattern || '%';
        END;
        $$ LANGUAGE plpgsql;
        """,
        """
        CREATE TEMPORARY TABLE IF NOT EXISTS temp_users (
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            phone_number VARCHAR(20)
        )
        """,
        """
        CREATE OR REPLACE PROCEDURE insert_many_users()
        LANGUAGE plpgsql
        AS $$
        DECLARE
            user_row RECORD;
        BEGIN
            FOR user_row IN SELECT * FROM temp_users LOOP
                IF LENGTH(user_row.phone_number) != 11 THEN
                    INSERT INTO incorrect_phone_numbers (first_name, last_name, phone_number)
                    VALUES (user_row.first_name, user_row.last_name, user_row.phone_number);
                ELSE
                    INSERT INTO contacts (first_name, last_name, phone_number)
                    VALUES (user_row.first_name, user_row.last_name, user_row.phone_number);
                END IF;
            END LOOP;
        END;
        $$;
        """,
        """
        CREATE TABLE IF NOT EXISTS incorrect_phone_numbers (
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            phone_number VARCHAR(20)
        )
        """
    )
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Проверяем наличие таблиц, функций, временной таблицы и процедуры перед их созданием
                for command in commands:
                    try:
                        cur.execute(command)
                    except Exception as e:
                        print("Error executing command:", e)
                        conn.rollback()
        print("Tables, function, temporary table, and procedure created successfully.")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error:", error)

if __name__ == '__main__':
    create_tables()
