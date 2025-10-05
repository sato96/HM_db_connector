# HM DB Connector

A lightweight MySQL database connector designed for microservices architecture of Home Manager ecosystme

## Features

- Simple and clean MySQL database operations
- Type-hinted methods for better IDE support
- Custom exception handling
- Connection management with auto-closing
- Support for basic operations (query, update, insert)

## Installation

Install directly from GitHub:

```bash
pip install git+https://github.com/your-username/HM_db_connector.git
```

## Usage

Basic usage example:

```python
from HM_db_connector import MysqlConnector

# Initialize the connector
db = MysqlConnector(
    host="localhost",
    database="your_database",
    username="your_username",
    password="your_password"
)

# Query example
try:
    results = db.query("SELECT * FROM users")
    for row in results:
        print(row)
except DatabaseError as e:
    print(f"Database error occurred: {e}")

# Insert example
try:
    db.insert("INSERT INTO users (name, email) VALUES ('John', 'john@example.com')")
except DatabaseError as e:
    print(f"Insert failed: {e}")

# Update example
try:
    db.update("UPDATE users SET name = 'Jane' WHERE id = 1")
except DatabaseError as e:
    print(f"Update failed: {e}")
```

## Error Handling

The library uses a custom `DatabaseError` exception that wraps MySQL connector errors. It's recommended to always wrap database operations in try-except blocks.

## Requirements

- Python 3.6+
- mysql-connector-python

## License

[Your chosen license]

## Contributing

Feel free to open issues or submit pull requests.