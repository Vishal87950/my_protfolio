import sqlite3
import pandas as pd

def export_to_excel():
    conn = sqlite3.connect('contacts.db')
    df = pd.read_sql_query('SELECT * FROM contacts', conn)
    df.to_excel('contacts.xlsx', index=False)
    conn.close()
    print("Exported contacts to contacts.xlsx")

if __name__ == '__main__':
    export_to_excel()
