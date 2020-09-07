import pandas
import mysql.connector
import Constants

CSV_FILE_PATH = "csv/data.csv"


def main():
    connection = mysql.connector.connect(user=Constants.USER, password=Constants.PASSWORD, host=Constants.HOST,
                                         port=Constants.PORT,
                                         database=Constants.DATABASE_NAME, charset="utf8")

    try:

        cursor = connection.cursor(prepared=True)

        try:

            # extract exists primary keys.
            cursor.execute("SELECT %s FROM %s" % (Constants.TABLE_PRIMARY_KEY_NAME, Constants.TABLE_NAME))
            existsKeys = [item[0] for item in cursor.fetchall()]

            # read csv file.
            csv_data = pandas.read_csv(CSV_FILE_PATH)

            # delete exists rows.
            updatableKeys = []
            columnName = get_csv_column_name(csv_data.keys().values, Constants.TABLE_PRIMARY_KEY_NAME)
            for index, row in csv_data.iterrows():
                if row[columnName] in existsKeys:
                    updatableKeys.append(row[columnName])
            if len(updatableKeys) > 0:
                deleteStatement = "DELETE FROM %s WHERE " % Constants.TABLE_NAME
                for index in range(len(updatableKeys)):
                    deleteStatement += (" OR " if (index > 0) else "") + "%s = ?" % (
                        Constants.TABLE_PRIMARY_KEY_NAME)
                cursor.execute(deleteStatement, updatableKeys)

            # insert data.
            for index, row in csv_data.iterrows():
                cursor.execute(
                    "INSERT INTO %s (%s) VALUES (%s)" % (
                        Constants.TABLE_NAME, ",".join(row.keys().values),
                        ",".join(["?" for _ in row.values])),
                    tuple(row.values))

            # commit data
            connection.commit()

        finally:
            # close connection
            cursor.close()

    finally:
        # close connection
        connection.close()


def get_csv_column_name(csv_column_names, key_name: str):
    index = [key.lower() for key in csv_column_names].index(key_name.lower())
    return csv_column_names[index]


if __name__ == "__main__":
    main()

# pandas#to_sql can't check any column data is already exists or not.
# "if_exists='replace'" option's effect is that drop the table before inserting new values.
# ref : https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html
