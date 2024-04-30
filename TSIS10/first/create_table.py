import psycopg2
from config import load_config

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE "user" (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL,
            level INTEGER DEFAULT 1
        )
        """,
        """
        CREATE TABLE user_score (
            score_id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES "user" (user_id) ON DELETE CASCADE,
            score INTEGER NOT NULL,
            level INTEGER NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE contacts (
            contact_id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100),
            phone_number VARCHAR(20) NOT NULL,
            email VARCHAR(255),
            address VARCHAR(255)
        )
        """
    )
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statements
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()
