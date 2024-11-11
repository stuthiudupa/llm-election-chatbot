"""
Runtime that accepts a sql statement and runs it on sql server.
Returns the results of sql execution.
"""
import traceback
import sqlite3

# MODIFY THE PATH BELOW FOR YOUR SYSTEM
my_db = r"your path"

class SQLRuntime(object):
    def __init__(self, dbname=None):
        if dbname is None:
            dbname = my_db
        conn = sqlite3.connect(dbname)  # creating a connection
        self.cursor = conn.cursor()  # we need the cursor to execute statement
        return

    def list_tables(self):
        result = self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
        table_names = sorted(list(zip(*result))[0])
        return table_names

    def get_schema_for_table(self, table_name):
        result = self.cursor.execute("PRAGMA table_info('%s')" % table_name).fetchall()
        column_names = list(zip(*result))[1]
        return column_names

    def get_schemas(self):
        schemas = {}
        table_names = self.list_tables()
        for name in table_names:
            fields = self.get_schema_for_table(name)  # fields of the table name
            schemas[name] = fields
        return schemas

    def execute(self, statement):
        code = 0
        msg = {
            "text": "SUCCESS",
            "reason": None,
            "traceback": None,
        }
        data = None

        try:
            self.cursor.execute(statement)
        except sqlite3.OperationalError:
            code = -1
            msg = {
                "text": "ERROR: SQL execution error",
                "reason": "possibly due to incorrect table/fields names",
                "traceback": traceback.format_exc(),
            }

        if code == 0:
            data = self.cursor.fetchall()

        msg["input"] = statement

        result = {
            "code": code,
            "msg": msg,
            "data": data
        }

        return result

    def execute_batch(self, queries):
        results = []
        for query in queries:
            result = self.execute(query)
            results.append(result)
        return results

    def post_process(self, data):
        """
        post process the data so that we can identify any harmful code and remove them.
        Also, llm output may need an output parser.
        :param data:
        :return:
        """
        # IMPLEMENT YOUR CODE HERE FOR POST-PROCESSING and VALIDATION
        return data


def sql_runtime(statement):
    """
    Instantiates a sql runtime and executes the given sql statement
    :param statement: sql statement
    """
    SQL = SQLRuntime()
    data = SQL.execute(statement)
    return data


if __name__ == '__main__':
    stmt = """
    SELECT * FROM elections_2019;
    """
    # stmt = input("Enter stmt: ")
    sql = SQLRuntime()
    data1 = sql.execute(stmt)

    dat = data1["data"]
    if dat is not None and len(dat) > 0:
        for record in dat:
            print(record)
            print("-" * 100)


