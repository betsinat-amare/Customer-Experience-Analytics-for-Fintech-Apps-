# src/load_to_postgres.py

import pandas as pd
import psycopg2
from psycopg2.extras import execute_batch

DB_CONFIG = {
    "host": "localhost",
    "dbname": "google_reviews",
    "user": "review_user",
    "password": "your_password_here",  # <-- update this
    "port": 5432
}

CLEAN_CSV = "data/clean/clean_reviews.csv"


def load_data():
    print("Loading CSV...")
    df = pd.read_csv(CLEAN_CSV)

    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    sql = """
        INSERT INTO reviews (review, rating, date, bank, source)
        VALUES (%s, %s, %s, %s, %s)
    """

    rows = list(df.itertuples(index=False, name=None))

    print("Inserting data into PostgreSQL...")

    # Manual batching
    batch_size = 500
    for i in range(0, len(rows), batch_size):
        batch = rows[i : i + batch_size]
        execute_batch(cur, sql, batch)
        print(f"Inserted batch {i // batch_size + 1}")

    conn.commit()
    cur.close()
    conn.close()

    print("✔ Data loaded successfully.")


if __name__ == "__main__":
    load_data()
