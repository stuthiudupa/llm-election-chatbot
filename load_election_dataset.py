import json
import sqlite3
import pandas as pd
import csv
from dbhelper import DbHelper


def load_data_from_csv(name, end=58925):
    data = []
    keys = None
    with open(name, "r", encoding="utf-8", errors="ignore") as f:
        csv_data = csv.reader(f)
        for i, line in enumerate(csv_data):
            if i == 0:
                keys = line
                continue
            item = {}
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


def create_dbs(docs_2019, docs_2024):
    dbh_2019 = DbHelper("elections_2019")
    for doc in docs_2019:
        _id = dbh_2019.insert_one(doc, "elections_2019")
        print(type(_id), _id)
    dbh_2024 = DbHelper("elections_2024")
    for doc in docs_2024:
        _id = dbh_2024.insert_one(doc, "elections_2024")
        print(type(_id), _id)
    return


if __name__ == '__main__':
    # create a connection to sql db called elections.db
    conn = sqlite3.connect('elections.db')

    # load the data into sqlite db
    filename_2019 = r"cleaned_csv/clean_ele_2019.csv"
    filename_2024 = r"cleaned_csv/clean_ele_2024.csv"
    data_2019 = load_data_from_csv(filename_2019, end=5)
    data_2024 = load_data_from_csv(filename_2024, end=5)
    # print(data[0])
    create_dbs(data_2019, data_2024)

    # res = load_data_from_csv_to_db(filename, conn)
    # print(res)

    query = 'SELECT party_name, COUNT(*) FROM elections_2019 GROUP BY party_name;'
    results = query_sql(conn, query)
    print(results)

    query = 'SELECT party_name, COUNT(*) FROM elections_2024 GROUP BY party_name;'
    results = query_sql(conn, query)
    print(results)

    # keys = data.keys()
    # for i, item in enumerate(data):
    #     print(data[item])
    # jdata = json.loads(data.to_json())
    # print(jdata)

