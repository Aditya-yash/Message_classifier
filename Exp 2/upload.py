import pandas as pd
import pymysql

# Database connection
db = pymysql.connect(
    host='localhost',
    user='root',
    password='Aditya@2003',
    database='mydb'
)
cursor = db.cursor()

# Read Excel file
df = pd.read_excel(r'C:\Users\Aditya Shrivastava\Desktop\health informatics\Exp 2\medical_data_updated.xlsx')

# Create new table
cursor.execute("DROP TABLE IF EXISTS patients")
create_query = """
CREATE TABLE patients (
    ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT,
    Gender VARCHAR(10),
    Mobile VARCHAR(15),
    Weight FLOAT,
    Height FLOAT,
    Disease VARCHAR(100),
    Treatment VARCHAR(100),
    Amount_Paid FLOAT
)
"""
cursor.execute(create_query)

# Insert data
insert_query = """
INSERT INTO patients (ID, Name, Age, Gender, Mobile, Weight, Height, Disease, Treatment, Amount_Paid)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
for _, row in df.iterrows():
    cursor.execute(insert_query, tuple(row))

db.commit()
cursor.close()
db.close()
print("Updated Excel data loaded into MySQL.")
