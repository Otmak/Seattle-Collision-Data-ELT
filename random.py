# print('Entering Models.py!!!')
# from typing import List
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Integer, String, ForeignKey, create_engine
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

# engine = create_engine("postgresql://localhost/portfolio_db_test_1")
# print('Starting....')


# declarative base class

# declarative base class
# class Base(DeclarativeBase):
#     pass
#
#
# print('Base class done.......')

# class User(Base):
#     __tablename__ = "test_user"
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str]
#     email: Mapped[str]
#     address: Mapped[List["Address"]] = relationship()
#     company: Mapped[List["Company"]] = relationship()
#
#     def __repr__(self):
#         return f'User(id={self.id}, name={self.name}, email={self.email})'
#
# print('USER table DONE!.......')
#
# class Address(Base):
#     __tablename__ = "address"
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     street: Mapped[str]
#     city: Mapped[str]
#     user_id: Mapped[int] = mapped_column(ForeignKey("test_user.id"))
#
#     def __repr__(self):
#         return f'Address(id={self.id}, street={self.street}, city={self.city}, user_id={self.user_id})'
#
# print('ADRESS table DONE!........')
# class Company(Base):
#     __tablename__ = "company"
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str]
#     catch_phrase: Mapped[str]
#     user_id: Mapped[int] = mapped_column(ForeignKey("test_user.id"))
#
#     def __repr__(self):
#         return f'Company(id={self.id}, name={self.name}, catch_phrase={self.catch_phrase}, user_id={self.user_id})'
# print('COMPANY table DONE!........')

# print('Tables class created ===>')

# Base.metadata.create_all(engine)
# print('DB Table created.....!')
# # user_data = Testuser(name='mr money', nickname='I have no nickname')
# my_data = [{'name': 'chuck rodes', 'nickname': 'Atorney for SD'},{'name': 'Mike prince', 'nickname': 'the once guy'},{'name': 'Waggs', 'nickname': 'the second man'},{'name': 'Wendy rodes', 'nickname': 'mistress'},{'name': 'Mason taylor', 'nickname': 'They them'}]
# j = 0
# for i in my_data:
#     print('ITER:', i, i['name'], i['nickname'])

#     with Session(engine) as session:
#         user_data = Testuser(id=f'THEID{j}' ,name=i['name'], nickname=i['nickname'])
#         session.add(user_data)
#         session.commit()
#     j+=1

# print('User added to Table!.........')
# print('Done')
