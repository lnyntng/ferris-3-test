import ferris3
import endpoints
import protopigeon
import logging

from protorpc import messages
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine('mysql://root@localhost/test')
DBSession = sessionmaker(bind=engine)
session = DBSession()


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    correo = Column(String(64), primary_key=True)
    clave = Column(String(32), nullable=False)
    username = Column(String(64), nullable=False)


UserMessage = protopigeon.model_cloudsql_message(User, key_field='correo')
# class UserMessage(messages.Message):
#     correo = messages.StringField(1)
#     clave = messages.StringField(2)
#     username = messages.StringField(3)


UserListMessage = protopigeon.list_message(UserMessage)
# class UserListMessage(messages.Message):
#     items = messages.MessageField(UserMessage, 1, repeated=True)


def rows_to_dict(rows):
    records = []
    for row in rows:
        d = {}
        for column in row.__table__.columns:
            d[column.name] = str(getattr(row, column.name))
        records.append(d)

    return records


def serialize_cloudsql_list(listMessage, data):
    rowsDict = rows_to_dict(data)
    list_message = listMessage()
    MessageType = listMessage.items.message_type
    list_message.items = [protopigeon.to_cloudsql_message(x, MessageType) for x in rowsDict]
    return list_message


@ferris3.auto_service
class CloudSqlService(ferris3.Service):

    @ferris3.auto_method(name="get_users", returns=UserListMessage)
    def get_users(self, request):
        users = session.query(User).all()
        return serialize_cloudsql_list(UserListMessage, users)

    @ferris3.auto_method(name="get_user", returns=UserListMessage)
    def get_user(self, request, email=(str,)):
        users = session.query(User).filter(User.correo == email).all()
        return serialize_cloudsql_list(UserListMessage, users)
