# What are connection methods?
cursor()  # - returns a new cursor object
commit()  # - any pending transaction to the database
rollback()  # - causes the database to roll back to the start of pending transaction
close()  # - close database connection


# What are cursor methods?
callproc()
execute()
executemany()
fetchone()
fetchmany()
fetchall()
nextset()
Arraysize()
close()

# Writing code using DB-API
# 0. Import
# from dbmodule import connect

# 1. - Create connection object
Connection = connect('databasename', 'username, pswd')

# 2. - Create a cursor object
Cursor = connection.cursor()

# 3. Run Queries
Cursor.execute('select * from mytable')
Results = cursor.fetchall()

# 4. Free resources
Cursor.close()
Connection.close()


# ibm_db API
# 1. import ibm_db
# 2. dsn_driver = "ibm db2 odbc driver"
# 3. dsn_database = "test"
# 4. dsn_hostname = "example"
# 5. dsn_port = "50001"
# 6. dsn_protocol = "TCPIP"
# 7. dsn_uid = "dash*****"
# 8. dsn_pwd = "*******"
