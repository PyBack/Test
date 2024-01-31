from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "mysql+pymysql://유저 이름:비밀번호@호스트 이름/db 이름",
        encoding="utf8",
    )
conn = engine.connect()
result_df = pd.read_sql_query(query, conn)
conn.close()
