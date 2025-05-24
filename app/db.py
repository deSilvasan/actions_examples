import mysql.connector

def get_mysql_version():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="example",
        database="testdb"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT VERSION();")
    print("MySQL version:", cursor.fetchone()[0])
    cursor.close()
    conn.close()

if __name__ == "__main__":
    get_mysql_version()

