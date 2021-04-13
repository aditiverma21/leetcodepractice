import redis

class DBconnection:
    connection=None

    @classmethod
    def get_connection(cls,new=False):
        #"creates return new singleton database connection"
        if new or not cls.connection:
            cls.connection=redis.Redis(host='192.168.0.164',port=6379,db=0)
        return cls.connection

    @classmethod
    def execute_query(cls,query):
        #"execute query on singleton Db connection"
        connection = cls.get_connection()
        try:
            connection.mset(query)
        except:
            connection = cls.get_connection(new=True) #create new connection
            connection.mset(query)

        connection.save()
        result = connection.keys("*")
        return result

    @classmethod
    def fetch_data(cls,key):
        connection = cls.get_connection()
        try:
            out=connection.get(key)
        except:
            connection = cls.get_connection(new=True)  # create new connection
            out=connection.get(key)

        return out

#print(DBconnection.execute_query({"Country": "{'India','Ireland','England','America'}"}))
print(DBconnection.fetch_data("Profile"))
