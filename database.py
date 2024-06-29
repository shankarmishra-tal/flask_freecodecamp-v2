
from sqlalchemy import create_engine
from sqlalchemy import text
from config import Config

# Create a SQLAlchemy engine using the MySQL credentials
engine = create_engine(f"mysql+pymysql://{Config.MYSQL_USERNAME}:{Config.MYSQL_PASSWORD}@{Config.MYSQL_HOST}:13820/{Config.MYSQL_DB_NAME}?charset=utf8mb4")


# Fetch all records from the jobs table in a dictionary format
def load_jobs():
        
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        # print(type(result.all()))
        result_all = result.fetchall()
        keys = result.keys()
        # print (result_all)
        result_all_dict = [dict(zip(keys, row)) for row in result_all]
    return result_all_dict