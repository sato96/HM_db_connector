import mysql.connector
from mysql.connector import Error
from typing import List, Dict, Any

class DatabaseError(Exception):
    """Custom exception for database operations"""
    pass

class MysqlConnector:
    def __init__(self, host: str, database: str, username: str, password: str):
        self._host = host
        self._database = database
        self._username = username
        self._password = password
        self._connection = None

    def query(self, text: str) -> List[Dict[str, Any]]:
        try:
            self._connect()
            if self._connection.is_connected():
                cursor = self._connection.cursor()
                cursor.execute(text)
                result = cursor.fetchall()
                r = [
                    {cursor.column_names[col]: row[col] 
                     for col in range(len(cursor.column_names))}
                    for row in result
                ]
                return r

        except Error as e:
            raise DatabaseError(f"Query failed: {str(e)}") from e
        finally:
            if self._connection and self._connection.is_connected():
                cursor.close()
                self._connection.close()

    def update(self, text: str):
        try:
            self._connect()
            if self._connection.is_connected():
                cursor = self._connection.cursor()
                cursor.execute(text)
                self._connection.commit()
                return cursor.fetchall()

        except Error as e:
            raise DatabaseError(f"Update failed: {str(e)}") from e
        finally:
            if self._connection and self._connection.is_connected():
                cursor.close()
                self._connection.close()

    def insert(self, text: str):
        try:
            self._connect()
            if self._connection.is_connected():
                cursor = self._connection.cursor()
                cursor.execute(text)
                self._connection.commit()
                return cursor.fetchall()

        except Error as e:
            raise DatabaseError(f"Insert failed: {str(e)}") from e
        finally:
            if self._connection and self._connection.is_connected():
                cursor.close()
                self._connection.close()