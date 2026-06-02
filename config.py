"""
Database Configuration File
Keep your database credentials here
"""

# SQL Server Configuration
DB_CONFIG = {
    'SERVER': 'Neha\\SQLEXPRESS',  # Change to your server name/IP (use (local) for local instance)
    'DATABASE': 'studentdb',  # Your database name
    'USE_WINDOWS_AUTH': True,  # Set to True for Windows Authentication (recommended), False for SQL Server auth
    'USERNAME': 'neha',  # Your username (only needed if USE_WINDOWS_AUTH is False)
    'PASSWORD': '',  # Your password (only needed if USE_WINDOWS_AUTH is False)
    'DRIVER': '{ODBC Driver 17 for SQL Server}'
}

# SQLAlchemy Connection String (for Windows Authentication)
SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://@{DB_CONFIG['SERVER']}/{DB_CONFIG['DATABASE']}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"

# Alternative: SQLAlchemy Connection String (for SQL Server Authentication)
# Uncomment this if using SQL Server authentication instead of Windows auth
# SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://{DB_CONFIG['USERNAME']}:{DB_CONFIG['PASSWORD']}@{DB_CONFIG['SERVER']}/{DB_CONFIG['DATABASE']}?driver=ODBC+Driver+17+for+SQL+Server"
