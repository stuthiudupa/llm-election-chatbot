"""
Loads Maharashtra assembly 2019 dataset
"""
import json
import sqlite3
import pandas as pd
import csv
# from dbhelper import DbHelper


def load_data_from_csv(name, end=58925):
    data = []
    keys = None
    with open(name, "r", encoding="utf-8") as f:
        csv_data = csv.reader(f)
        for i, line in enumerate(csv_data):
            found = False
            if i == 0:
                keys = line
                continue
            for field in line:
                if field.strip() == "TURNOUT":
                    found = True
                    break
            if found:
                print("TURNOUT found, skipping")
                continue
            item = {}
            print(line)
            for key, val in zip(keys, line):
                item[key] = val
            data.append(item)
    return data


def load_data_from_csv_to_db(name, conn):

    # read the dataset from csv file and create a pandas dataframe
    df = pd.read_csv(open(name, "r", encoding="utf-8"))

    # save the dataframe as a database table, name of table is: elections_2019
    result = df.to_sql("elections_2019", conn)

    return result


def query_sql(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    field_names = [r[0] for r in cursor.description]
    print(field_names)
    return result


# def create_db(docs):
#     dbh = DbHelper()
#     for doc in docs:
#         _id = dbh.insert_one(doc)
#         print(type(_id), _id)
#     return


if __name__ == '__main__':
    # create a connection to sql db called elections.db
    # conn = sqlite3.connect('elections.db')

    filename = r"maha_results_2019.csv"
    data = load_data_from_csv(filename, end=5)
    # print(data)

    # # print(data)
    # create_db(data)

    # res = load_data_from_csv_to_db(filename, conn)
    # print(res)

    # query = "SELECT * FROM elections_2019 WHERE [State-UT Code & Name]='Andhra Pradesh';"
    # results = query_sql(conn, query)
    # print(results)

    # keys = data.keys()
    # for i, item in enumerate(data):
    #     print(data[item])
    # jdata = json.loads(data.to_json())
    # print(jdata)

