import sqlite3

# Establish connection to the database
db_name = "users.db"
conn = sqlite3.connect(db_name)
print("Opened database successfully")

# Define and execute the SQL query to create the table
conn.execute('''CREATE TABLE employees (
                ID INT PRIMARY KEY NOT NULL,
                NAME VARCHAR(1000) NOT NULL,
                AGE INT NOT NULL,
                ADDRESS TEXT,
                SALARY FLOAT
                )''')

# Commit changes and close connection
conn.commit()
conn.close()