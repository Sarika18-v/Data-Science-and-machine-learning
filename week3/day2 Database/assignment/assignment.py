import sqlite3

# Establish connection to the database
db_name = "userss.db"
conn = sqlite3.connect(db_name)
print("Opened database successfully")

# Define and execute the SQL query to create the table
conn.execute('''CREATE TABLE user Registration(
                Username  VARCHAR(1000) NOT NULL,
                Email NOT NULL,
                Password NOT NULL,
                )''')
def register user(username,password):
    
    
# Commit changes and close connection
conn.commit()
conn.close()