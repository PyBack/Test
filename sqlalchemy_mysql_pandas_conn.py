from sqlalchemy import create_engine
import pandas as pd

mysql_user_name = ''
mysql_pw = ''
mysql_hostname = ''

# url = "mysql+pymysql://[id]:[pw]@[mysql주소]:[port]/[db_name]?charset=utf8"
url = f"mysql+pymysql://{mysql_user_name}:{mysql_pw}@{mysql_hostname}:{port}/mysql?charset=utf8"

engine = create_engine(
    url=url,
    )
conn = engine.connect()
sql_text = """
show databases;
"""
result_df = pd.read_sql_query(sql_text, conn)
print(result_df)
conn.close()
