import datetime
import mysql.connector

# when we are not creating ay input argument then its better to create singleton design pattern
class DB1Connection:
    connection=None

    #We want to protect our program from being instantiated directly we want to use class bound method
    #we implemented singleton design pattern to make sure one instance of connection get created
    #
    @classmethod
    def get_connection(cls,new=False):
        if new or not cls.connection:
            connection = mysql.connector.connect(user='abcd', database='P01')
        return cls.connection

    @classmethod
    def get_count(cls):
        connection = cls.get_connection()
        try:
            cursor = connection.cursor()
        except:
            connection = cls.get_connection(new=True)
            cursor = connection.cursor()
        query = ("SELECT count(spid) FROM server1.po1")
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    #flip script changes the DNS entry of the DB1 and DB2 Ip address