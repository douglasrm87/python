import pyodbc
import pandas as pd

  # connect odbc to data source name
conn = pyodbc.connect("DSN=<your_dsn>", autocommit=True)

  # read data into dataframe
hive_df = pd.read_sql("SELECT * FROM <table_name>", conn)