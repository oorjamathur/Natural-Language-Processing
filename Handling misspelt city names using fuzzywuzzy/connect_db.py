import mysql.connector
import pandas as pd
def db_connect(pwd,db,host='localhost',user='root'):
  db_connection = mysql.connector.connect(
    host=host,
    user=user,
    passwd=pwd,
    database=db
  )
  my_database = db_connection.cursor()
  sql_statement = "SELECT * FROM cities"
  my_database.execute(sql_statement)
  output = my_database.fetchall()
  df = pd.DataFrame(output)
  df.columns=['city']
  if (df.empty==False):
    return df
  return None
