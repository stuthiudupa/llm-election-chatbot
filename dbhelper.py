# dbhelper.py
import sqlite3

class DbHelper:
    def __init__(self, table_name, db_name="elections.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table(table_name)

    def create_table(self, table_name):
        if table_name == "elections_2024":
            # Create the elections_2024 table if it doesn't exist
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS elections_2024 (
            candidate_name TEXT,
            party_name TEXT,
            general_votes INTEGER,
            postal_votes INTEGER,
            secured_votes INTEGER,
            percentage_of_votes REAL,
            state_name TEXT,
            constituency_name TEXT
        )
        '''
        elif table_name == "elections_2019":
            # Create the elections_2019 table if it doesn't exist
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS elections_2019 (
            state_name TEXT,
            parlimentary_constituency_name TEXT,
            assembly_constituency_name TEXT,
            nota_votes INTEGER,
            candidate_name TEXT,
            party_name TEXT,
            votes_secured REAL
        )
        '''
        elif table_name == "maha_2019":
            # Create the maha_2019 table if it doesn't exist
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS maha_2019 (
            state_name TEXT,
            assembly_constituency_number INTEGER,
            assembly_constituency_name TEXT,
            candidate_name TEXT,
            sex TEXT,
            age INTEGER,
            category TEXT,
            party_name TEXT,
            party_symbol TEXT,
            general_votes INTEGER,
            postal_votes REAL,
            secured_votes INTEGER,
            percentage_votes_polled REAL,
            total_voters REAL
        )
        '''
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def insert_one(self, document, table_name):
        keys = ', '.join(document.keys())
        question_marks = ', '.join(['?'] * len(document))
        values = tuple(document.values())
        query = f'INSERT INTO {table_name} ({keys}) VALUES ({question_marks})'
        self.cursor.execute(query, values)
        self.conn.commit()
        return self.cursor.lastrowid

    def close(self):
        self.conn.close()
