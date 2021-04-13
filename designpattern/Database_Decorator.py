#using Decorator to create and close a connection to a database

import sqlite3
from functools import wraps

def with_connection(f):
    @wraps(f)
    def wrapped(*args,**kwargs):
        conn = sqlite3.connect("dec.db")
        cursor = conn.cursor()
        f_ret = f(cursor,*args,**kwargs)
        conn.commit()
        conn.close()
        return f_ret
    return wrapped

@with_connection
def init_db(cursor):
    sql=( 'CREATE TABLE IF NOT EXISTS person ('
          ' name text Not Null,'
          ' phone text Not Null'
          ')'
          )
    cursor.execute(sql)

@with_connection
def add_person(cursor, name,phone):
    sql = 'INSERT INTO person VALUES (?,?)'
    cursor.execute(sql,(name,phone))

@with_connection
def get_everyone(cursor):
    sql = "SELECT * FROM person"
    cursor.execute(sql)
    return cursor.fetchall()

@with_connection
def remove_person(cursor,name,phone):
    sql = """Delete from person where name = ? and phone = ?"""
    cursor.execute(sql,(name,phone))

'''
@with_connection
def remove_table(cursor,tablename):
    sql = "DROP table (?)"
    cursor.execute(sql,(tablename))
    print(f"Successfully deleted the table {tablename}")
'''
def create_directory(file):
    with open(file,'r') as entries:
        for entry in entries:
            each_record = entry.split("")
            add_person(each_record[0],each_record[1])



if __name__ == '__main__':
    #init_db()
    #add_person("Aditi","899886431")
    #create_directory("phone_book.txt")
    remove_person("\"Vidhya\"","\"353892360694\"")
    #remove_table("person")

    for name, phone in get_everyone():
        print(name, phone)