import pandas
import mysql.connector
import Constants

CSV_FILE_PATH = "csv/data.csv"

mysql_config = {
    'user': Constants.USER,
    'password': Constants.PASSWORD,
    'host': Constants.HOST,
    'port': Constants.PORT,
    'database': Constants.DATABASE_NAME,
    'charset': 'utf8'
}


def main():
    connection = mysql.connector.connect(user=Constants.USER, password=Constants.PASSWORD, host=Constants.HOST,
                                         port=Constants.PORT,
                                         database=Constants.DATABASE_NAME, charset="utf8")

    try:

        # extract exists gu_id.
        cursor = connection.cursor(buffered=True)

        try:

            cursor.execute("SELECT %s FROM %s" % (Constants.TABLE_PRIMARY_KEY_NAME, Constants.TABLE_NAME))
            existsKeys = [item[0] for item in cursor.fetchall()]

            # read csv file.
            csv_data = pandas.read_csv(CSV_FILE_PATH)

            # delete exists rows.
            updatableKeys = []
            for index, row in csv_data.iterrows():
                if row[Constants.TABLE_PRIMARY_KEY_NAME] in existsKeys:
                    updatableKeys.append(row[Constants.TABLE_PRIMARY_KEY_NAME])
            if len(updatableKeys) > 0:
                deleteStatement = "DELETE FROM %s WHERE " % Constants.TABLE_NAME
                for index in range(len(updatableKeys)):
                    deleteStatement += (" OR " if (index > 0) else "") + "%s = %s" % (
                        Constants.TABLE_PRIMARY_KEY_NAME, "%s")
                cursor.execute(deleteStatement, updatableKeys)

            # insert data.
            for index, row in csv_data.iterrows():
                cursor.execute(
                    "INSERT INTO %s (%s) VALUES (%s)" % (
                        Constants.TABLE_NAME, ",".join(row.keys().values),
                        ",".join(["'" + item + "'" for item in row.values])))

            # commit data
            connection.commit()

        finally:
            # close connection
            cursor.close()

    finally:
        # close connection
        connection.close()


if __name__ == "__main__":
    main()

# pandas#to_sql can't check any column data is already exists or not.
# "if_exists='replace'" option's effect is that drop the table before inserting new values.
# ref : https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html
