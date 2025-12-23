from database import get_db_connection


def init_db():
    """
    Create the menu_items table if it doesn't already exist.
    This is a simple setup script so the app has some data structure to work with.
    """
    conn = None
    try:
        conn = get_db_connection()
        if conn is None:
            print("Could not connect to the database.")
            return

        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS menu_items (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(100),
                        price NUMERIC(10, 2)
                    );
                    """
                )
                print("Table 'menu_items' created or already exists.")

    except Exception as e:
        print("Error initialising DB:", e)

    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    init_db()
