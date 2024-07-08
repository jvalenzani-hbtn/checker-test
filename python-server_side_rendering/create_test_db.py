import sqlite3

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (24, 'Jarvis', 'Electronics', 799.99),
        (78, 'Tesla Coil', 'Home Appliances', 6.99)
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()