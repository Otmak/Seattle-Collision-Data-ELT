print('LOAD called!.....')
import urllib.request
import json


class Load():
    """docstring for Load"""

    def __init__(self, tables, db, data):
        self.tables = tables
        self.db = db
        self.data = data

    def get_columns(self, table):
        return [column.key for column in table.__table__.columns]

    def load_data(self):
        print('Starting the LOADING.......')

        for i in self.data:

            for table in self.tables:
                print('TABLE NAME *******>', table)
                columns = self.get_columns(table)
                insert_data = table()

                for column in columns:
                    try:
                        key = column
                        value = i[column]
                        print(':', key, value)
                        setattr(insert_data, column, value)
                    except Exception as e:
                        print('ERROR:', e)
                print('====**>',table)
                print('****As inser_data INSTANCE', insert_data)
                self.db.session.add(insert_data)
                print('ADDED DATA!')
                self.db.session.commit()
                print('COMMITED DATA')

            print('==============================>')



        # for i in data:
        #     # print('ITER:', i, i['name'], i['nickname'])
        #     print('creating VARS............')
        #     user_data = self.user(id=i['id'], name=i['name'], email=i['email'])
        #     address_data = self.address(street=i['address']['street'], city=i['address']['city'], user_id=i['id'])
        #     company_data = self.company(name=i['company']['name'], catch_phrase=i['company']['catchPhrase'],
        #                                 user_id=i['id'])

        #     print('Done creating VARS')
        #     print('Created', user_data)
        #     print('creted', address_data)
        #     print('created', company_data)

        #     print('Starting Sessions')
        #     # with Session(engine) as session:
        #     self.db.session.add(user_data)
        #     self.db.session.add(address_data)
        #     self.db.session.add(company_data)
        #     self.db.session.commit()
        # print('WOW DONE DONE...... ====> ')
        return 'ALL DONE!'



