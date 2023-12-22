import urllib.request
import json


class Load():
    """Load data into the postgreSQL database"""

    def __init__(self, tables, db, data):
        self.tables = tables
        self.db = db
        self.data = data

    def get_columns(self, table):
        return [column.key for column in table.__table__.columns]

    def load_data(self):
        for i in self.data:
            for table in self.tables:
                columns = self.get_columns(table)
                insert_data = table()

                for column in columns:
                    try:
                        setattr(insert_data, column, i[column])
                    except Exception as e:
                        print("Couldn't add :", e)
                self.db.session.add(insert_data)
                self.db.session.commit()

        return 'DONE!'



