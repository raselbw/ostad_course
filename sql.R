library(DBI)

#2. Connect to the MySQL database

con <- dbConnect(RMySQL::MySQL(),
                 host = "192.168.142.10",      # you're already on the server
                 port = 3306,             # standard MySQL port
                 user = "rbiswas1",   # as in your Workbench
                 password = "asmani@123", 
                 dbname = NULL)  # default database for metadata

#3. List available databases

dbListDatabases(con)

#4. Use a specific database

dbExecute(con, "USE your_database_name;")


#5. Run a query and get the data

df <- dbGetQuery(con, "SELECT * FROM your_table LIMIT 10;")
head(df)
