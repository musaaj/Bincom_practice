from typing import List, Tuple
import re
import psycopg2

def extract_names(filename: str, db_config: dict) -> None:
    """
    Extracts baby names, ranks, and genders 
    from an HTML file containing US baby name data
    and saves them to a PostgreSQL database.

    Args:
        filename: A string representing the name of the HTML file.
        db_config: A dictionary containing the configuration
                   parameters for the PostgreSQL database,
                   including the host, port, database name,
                   username, and password.
    """
    try:
        with open(filename) as file:
            html = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f'{filename} does not exists')
    pattern = r'<td>(\d+)<\/td>\s*<td>(?:<.*?>)*([A-Za-z ]+)<\/td>\s*<td>(?:<.*?>)*(.*?)<\/td>'
    matches = re.findall(pattern, html)

    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS baby_names (
            id SERIAL PRIMARY KEY,
            year INTEGER,
            rank INTEGER,
            male_name VARCHAR(50) NOT NULL,
            female_name VARCHAR(50) NOT NULL
        );
    """)

    for rank, male_name, female_name in matches:
        cursor.execute("""
            INSERT INTO baby_names (year, rank, male_name, female_name)
            VALUES (%s, %s, %s, %s);
        """, (int(filename[-8:-5]), int(rank), male_name.strip(), female_name.strip()))

    conn.commit()
    conn.close()
