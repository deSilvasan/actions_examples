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
    version = cursor.fetchone()[0]
    print("MySQL version:", version)
    cursor.close()
    conn.close()
    return version

if __name__ == "__main__":
    get_mysql_version()

