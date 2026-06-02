# Student Management System - SQL Server & Python Connection

This project connects Python to SQL Server for student management operations.

## Prerequisites

1. **SQL Server** - Make sure SQL Server is installed and running
2. **ODBC Driver 17 for SQL Server** - [Download here](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server)
3. **Python 3.7+**

## Installation

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Update database credentials in `config.py`:**
   - Change `SERVER` to your SQL Server instance name
   - Update `DATABASE` with your database name
   - Set `USERNAME` and `PASSWORD` to your credentials

## Connection Methods

### Method 1: Using pyodbc (Direct)
```python
from db_connection import connect_with_pyodbc

conn = connect_with_pyodbc()
```

### Method 2: Using SQLAlchemy (ORM)
```python
from db_connection import create_sqlalchemy_engine

engine = create_sqlalchemy_engine()
```

## Quick Start

### 1. Test Connection
```bash
python db_connection.py
```

### 2. Execute a Query
```python
from db_connection import connect_with_pyodbc, execute_query

conn = connect_with_pyodbc()
results = execute_query(conn, "SELECT * FROM students")
for row in results:
    print(row)
conn.close()
```

### 3. Insert Data
```python
from db_connection import connect_with_pyodbc, execute_update

conn = connect_with_pyodbc()
query = "INSERT INTO students (name, email, phone) VALUES ('John Doe', 'john@example.com', '123-456-7890')"
execute_update(conn, query)
conn.close()
```

## Troubleshooting

### Connection Error: "ODBC Driver not found"
- Install ODBC Driver 17 for SQL Server
- Verify the driver name matches in your code

### Connection Error: "Login failed"
- Check username and password
- Verify SQL Server is running
- Check user permissions on the database

### Connection Error: "Server not found"
- Verify server name/IP address
- Check SQL Server Browser service is running
- Use `(local)` or `localhost` for local instances

## Files

- `db_connection.py` - Database connection functions
- `config.py` - Configuration settings
- `requirements.txt` - Python dependencies
- `README.md` - This file

## Next Steps

1. Create tables in SQL Server for your student management system
2. Implement database operations (CRUD - Create, Read, Update, Delete)
3. Add error handling and logging
4. Consider using SQLAlchemy models for better code organization
