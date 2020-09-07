import pandas
from sqlalchemy import create_engine
import Constants

CSV_FILE_PATH = "csv/data.csv"


def get_mysql_connection():
    return create_engine('mysql://%s:%s@%s:%s/%s' % (
        Constants.USER, Constants.PASSWORD, Constants.HOST, Constants.PORT, Constants.DATABASE_NAME))


with get_mysql_connection().begin() as connection:
    df = pandas.read_csv(CSV_FILE_PATH)
    df.to_sql(Constants.TABLE_NAME, connection, if_exists='append', index=None)
