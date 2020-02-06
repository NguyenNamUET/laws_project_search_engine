import psycopg2
from psycopg2 import pool
try:
    postgreSQL_pool = psycopg2.pool.SimpleConnectionPool(1, 20,user = "postgres",
                                              password = "12345678",
                                              host = "localhost",
                                              port = "5433",
                                              database = "lawtech")
    if(postgreSQL_pool):
        print("Connection pool created successfully")

    # Use getconn() to Get Connection from connection pool
    ps_connection  = postgreSQL_pool.getconn()
    #
    if(ps_connection):
        print("successfully recived connection from connection pool ")
        ps_cursor = ps_connection.cursor()
        ps_cursor.execute("select * from laws_extractivedocument limit 10")
        mobile_records = ps_cursor.fetchall()

        print ("Displaying rows from mobile table")
        for row in mobile_records:
            print (type(row))

        ps_cursor.close()

        #Use this method to release the connection object and send back to connection pool
        postgreSQL_pool.putconn(ps_connection)
        print("Put away a PostgreSQL connection")

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while connecting to PostgreSQL", error)

finally:
    #closing database connection.
    # use closeall method to close all the active connection if you want to turn of the application
    if (postgreSQL_pool):
        postgreSQL_pool.closeall
    print("PostgreSQL connection pool is closed")