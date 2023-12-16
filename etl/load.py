
class Load():
    """docstring for Load"""

    def __init__(self, tables, db, data):
        self.tables = tables
        self.db = db
        self.data = data

    def get_columns(self, table):
        return [column.key for column in table.__table__.columns]

    def load_data(self):

        for i in self.data: # Load 2.0
            for table in self.tables:
                columns = self.get_columns(table)
                for column in columns:
                    try:
                        print(':', column, i[column])
                    except Exception as e:
                        print('error:', e)
        return 
