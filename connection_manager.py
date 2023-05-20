import sqlite3


class ConnectionManager:

    def __init__(self, db_path: str, db_name: str):
        self.db_path = db_path
        self.db_name = db_name
        self.db_connection: sqlite3.Connection = None
        self.db_cursor: sqlite3.Cursor = None
        if self.db_connection is None:
            self.db_connection = sqlite3.connect(self.db_path)
        if self.db_cursor is None:
            self.db_cursor = self.db_connection.cursor()

    def get_db_path(self):
        return self.db_path

    def get_db_name(self):
        return self.db_name

    def get_db_connection(self):
        if self.db_connection == None:
            self.db_connection = sqlite3.connect(self.db_path)
        return self.db_connection

    def get_db_cursor(self):
        if self.db_cursor == None:
            self.db_cursor = self.db_connection.cursor()
        return self.db_cursor
