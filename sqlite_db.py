import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, db_file):
        # get connection
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
        except Error as e:
            print("(Database)", e)
            exit()

    def create_table(self, create_statement):
        try:
            cursor = self.conn.cursor()
            cursor.execute(create_statement)
        except Error as e:
            print("create_table ", e)
            
    def create_tables(self, create_statements: list):
        for create_statement in create_statements:
            self.create_table(create_statement)
            
    def execute(self, statement):
        try:
            cursor = self.conn.cursor()
            cursor.execute(statement)
            self.conn.commit()
        except Error as e:
            print("insert ", e)

    def execute_all(self, statements: list):
        for statement in statements:
            self.execute(statement)
            
    def query(self, query_statement) -> str:
        query_response = ""

        try:
            cursor = self.conn.cursor()
            cursor.execute(query_statement)
            
            rows = cursor.fetchall()
            for row in rows:
                query_response += str(row)
        except Error as e:
            print("query ", e)
            
        return query_response
