import MySQLdb
import pandas as pd
import numpy as np
import defs

def create_tables(db):
    with open("create_database.sql", "r") as file:
        create_table_operation = file.read()
    cursor = db.cursor()
    try:
        cursor.execute(create_table_operation)
        print("Build database %s : OK"% defs.database)
    except MySQLdb._exceptions.OperationalError:
        print("No database %s or tables have been created"%defs.database)

if __name__ == "__main__":
    db = MySQLdb.connect(defs.host, defs.user, defs.password, defs.database, charset="utf8")
    create_tables(db)    
