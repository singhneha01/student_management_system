"""
Test connection and list available databases
"""
import pyodbc

SERVER = 'Neha\\SQLEXPRESS'
USERNAME = 'neha'
PASSWORD = 'dragon@hell21'

try:
    # Connect to master database using Windows Authentication
    connection_string = f'Driver={{ODBC Driver 17 for SQL Server}};Server={SERVER};Database=master;Trusted_Connection=yes;'
    conn = pyodbc.connect(connection_string)
    print("✓ Connected to SQL Server!")
    
    # List all databases
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sys.databases ORDER BY name")
    databases = cursor.fetchall()
    
    print("\nAvailable databases:")
    for db in databases:
        print(f"  - {db[0]}")
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"✗ Error: {e}")
