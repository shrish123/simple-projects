import sqlite3
 
conn = sqlite3.connect("mydatabase.db") 
 
cursor = conn.cursor()
 

cursor.execute("""CREATE TABLE grp
                  (item text, quant integer) 
               """)
conn.close
