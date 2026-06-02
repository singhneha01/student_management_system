"""
SQL Server Database Connection Module
"""
import pyodbc
from sqlalchemy import create_engine

# Connection parameters
SERVER = 'Neha\\SQLEXPRESS'  # or your server name (use (local) for local instance)
DATABASE = 'studentdb'  # or your database name

# Option 1: Windows Authentication (Recommended - no password needed)
USE_WINDOWS_AUTH = True

# Option 2: SQL Server Authentication (if Windows Auth doesn't work)
USERNAME = ''  # your username
PASSWORD = ''  # your password (leave empty if using Windows Auth)

# Method 1: Using pyodbc (Direct Connection)
def connect_with_pyodbc():
    """
    Connect to SQL Server using pyodbc
    """
    try:
        if USE_WINDOWS_AUTH:
            # Windows Authentication (no password needed)
            connection_string = f'Driver={{ODBC Driver 17 for SQL Server}};Server={SERVER};Database={DATABASE};Trusted_Connection=yes;'
        else:
            # SQL Server Authentication (with username/password)
            connection_string = f'Driver={{ODBC Driver 17 for SQL Server}};Server={SERVER};Database={DATABASE};UID={USERNAME};PWD={PASSWORD}'
        
        conn = pyodbc.connect(connection_string)
        print("✓ Connected to SQL Server successfully using pyodbc!")
        return conn
    except Exception as e:
        print(f"✗ Error connecting to SQL Server: {e}")
        return None

# Method 2: Using SQLAlchemy (ORM - Recommended for larger projects)
def create_sqlalchemy_engine():
    """
    Create SQLAlchemy engine for SQL Server
    """
    try:
        if USE_WINDOWS_AUTH:
            # Windows Authentication
            connection_string = f'mssql+pyodbc://@{SERVER}/{DATABASE}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'
        else:
            # SQL Server Authentication
            connection_string = f'mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver=ODBC+Driver+17+for+SQL+Server'
        
        engine = create_engine(connection_string)
        print("✓ SQLAlchemy engine created successfully!")
        return engine
    except Exception as e:
        print(f"✗ Error creating SQLAlchemy engine: {e}")
        return None

# Example: Execute a query
def execute_query(conn, query):
    """
    Execute a SQL query and return results
    """
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results
    except Exception as e:
        print(f"✗ Error executing query: {e}")
        return None

# Example: Execute an update query
def execute_update(conn, query):
    """
    Execute an INSERT, UPDATE, or DELETE query
    """
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        print("✓ Query executed successfully!")
        cursor.close()
    except Exception as e:
        print(f"✗ Error executing update: {e}")
        conn.rollback()

if __name__ == "__main__":
    # Test connection
    conn = connect_with_pyodbc()
    if conn:
        # Example query
        results = execute_query(conn, "SELECT TOP 5 * FROM students")
        if results:
            for row in results:
                print(row)
        conn.close()
