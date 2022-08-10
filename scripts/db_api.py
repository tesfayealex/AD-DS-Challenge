import string
import pandas as pd
import numpy as np
import os
from logger import logger
from datetime import date, datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine, types, text

class Database_api:

    def __init__(self):
        load_dotenv()
        host_name=os.getenv('HOST_NAME')
        db_user=os.getenv('DB_USER')
        db_password=os.getenv('DB_PASSWORD')
        db_name= os.getenv('DB_NAME')
        self.postgres_engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{host_name}/{db_name}')
        
    def get_db_data_from_table_name(self,tablename: string = 'warehouse') -> list:
        try:
            data = pd.read_sql(f'SELECT * FROM public.{tablename}',self.postgres_engine)
            logger.info("successfully fetched the data")
            return data
        except Exception as e:
            logger.error(e)
            return pd.DataFrame()
    def store_db_data_using_table_name(self,df: pd.DataFrame , tablename: string = 'warehouse') -> list:
        try:
            data = df.to_sql(tablename, con=self.postgres_engine, if_exists='replace', index=False)
            logger.info("successfully stored the data")
            return True
        except Exception as e:
            logger.error(e)
            return False

if __name__ == "__main__":
        database = Database_api()
        warehouse = database.get_db_data_from_table_name('warehouse')
        print(warehouse.shape)
