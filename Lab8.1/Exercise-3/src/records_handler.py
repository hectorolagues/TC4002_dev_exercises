import sqlite3
from sqlite3 import Error
import logging


class RecordsHandler:
    def __init__(self, db_file):
        self.sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS Records (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        email text NOT NULL,
                                        age text NOT NULL,
                                        origin text NOT NULL
                                    ); """

        self.create_connection(db_file)

    def create_connection(self, db_file):
        """ create a database connection to a SQLite database """
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
            logging.basicConfig(format='\n%(levelname)s:%(message)s', level=logging.INFO)
            logging.info("Creating connection")
        except Error as e:
            print(e)
            logging.basicConfig(format='\n%(levelname)s:%(message)s', level=logging.INFO)
            logging.error("Connection not established with Database")

        self.create_table(self.sql_create_projects_table)

    def close_connection(self):
        if self.conn:
            self.conn.close()
            logging.basicConfig(format='\n%(levelname)s:%(message)s', level=logging.INFO)
            logging.info("The connection is closed")

    def create_table(self, create_table_sql):
        """create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
            self.conn.commit()
            logging.basicConfig(format='\n%(levelname)s:%(message)s', level=logging.INFO)
            logging.info("Table creation")
        except Error as e:
            print(e)
            logging.basicConfig(format='\n%(levelname)s:%(message)s', level=logging.INFO)
            logging.error("Table was not created")

    def add_record(self, name="", email="", age="", origin=""):
        sqlquery = "INSERT INTO Records (name, email, age, origin) VALUES ('%s', '%s', '%s', '%s')"
        val = (name, email, age, origin)
        query = sqlquery % val
        try:
            c = self.conn.cursor()
            c.execute(query)
            self.conn.commit()
            logging.basicConfig(format='\n%(levelname)s:%(message)s', level=logging.INFO)
            logging.info("Adding record")
        except Error as e:
            print(e)
            logging.basicConfig(format='\n%(levelname)s:%(message)s', level=logging.INFO)
            logging.error("The record was not added")

    def delete_record(self, record_id=-1):
        sqlquery = "DELETE FROM Records WHERE id='%s'"
        val = record_id
        query = sqlquery % val
        try:
            c = self.conn.cursor()
            c.execute(query)
            self.conn.commit()
            logging.basicConfig(format='\n%(levelname)s:%(message)s', level=logging.INFO)
            logging.info("Deleting record")
        except Error as e:
            print(e)
            logging.basicConfig(format='\n%(levelname)s:%(message)s', level=logging.INFO)
            logging.error("The record was not deleted")

    def look(self, email="", age=""):
        sqlquery = "SELECT * FROM Records WHERE email='%s' AND age='%s'"
        val = (email, age)
        query = sqlquery % val

        results = []
        try:
            c = self.conn.cursor()
            c.execute(query)
            results.extend(c.fetchall())
            logging.basicConfig(format='\n%(levelname)s:%(message)s', level=logging.INFO)
            logging.info("Looking for a specific record")
        except Error as e:
            print(e)
            logging.basicConfig(format='\n%(levelname)s:%(message)s', level=logging.INFO)
            logging.error("Not able to find the record")

        return results

    def list_all(self):
        query = "SELECT * FROM Records"
        results = []
        try:
            c = self.conn.cursor()
            c.execute(query)
            results.extend(c.fetchall())
            logging.basicConfig(format='\n%(levelname)s:%(message)s', level=logging.INFO)
            logging.info("Listing all the records")
        except Error as e:
            print(e)
            logging.basicConfig(format='\n%(levelname)s:%(message)s', level=logging.INFO)
            logging.error("Not able to list all the records")

        # loop through the rows
        for row in results:
            print(row)
    
    def delete_all(self):
        sqlquery = "DELETE FROM Records"
        try:
            c = self.conn.cursor()
            c.execute(sqlquery)
            self.conn.commit()
            logging.basicConfig(format='\n%(levelname)s:%(message)s', level=logging.INFO)
            logging.info("Deleting all the records")
        except Error as e:
            print(e)
            logging.basicConfig(format='\n%(levelname)s:%(message)s', level=logging.INFO)
            logging.error("Not able to delete all the records")
