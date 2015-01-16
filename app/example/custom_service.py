import ferris3
import endpoints
import protopigeon
from protorpc import messages
from google.appengine.ext import ndb
from google.appengine.ext.ndb import msgprop
from pprint import pprint
import MySQLdb
import _mysql
import json
import sqlalchemy


class StringTranslation(ndb.Model):
    english = ndb.StringProperty()
    spanish = ndb.StringProperty()
    portuguese = ndb.StringProperty()


class StringTranslationProperty(msgprop.MessageProperty):
    def __init__(self, **kwds):
        super(StringTranslationProperty, self).__init__(StringTranslationMessage, **kwds)


class ExampleProperty(ndb.StringProperty):
    def _to_base_type(self, value):
        return "---" + str(value) + "---"

    def _from_base_type(self, value):
        return value.strip('-')


class StringTranslationMessage(messages.Message):
    english = messages.StringField(1)
    spanish = messages.StringField(2)
    portuguese = messages.StringField(3)


class ExampleModel(ndb.Model):
    normal = ndb.StringProperty()
    custom = ExampleProperty()
    translation = StringTranslationProperty()


class SimpleModel(ndb.Model):
    simple = ndb.StringProperty()


class SimpleModelMessage(messages.Message):
    simple = messages.StringField(1)


class SimpleListMessage(messages.Message):
    items = messages.MessageField(SimpleModelMessage, 1, repeated=True)


class ExamplePropertyConverter(protopigeon.converters.Converter):
    @staticmethod
    def to_field(Model, property, count):
        return messages.StringField(count, repeated=property._repeated, required=property._required)


class StringTranslationPropertyConverter(protopigeon.converters.Converter):
    @staticmethod
    def to_field(Model, property, count):
        return messages.MessageField(StringTranslationMessage, count)

protopigeon.converters.converters["ExampleProperty"] = ExamplePropertyConverter
protopigeon.converters.converters["StringTranslationProperty"] = StringTranslationPropertyConverter


@ferris3.auto_service
class CustomService(ferris3.Service):
    list = ferris3.hvild.list(ExampleModel)
    insert = ferris3.hvild.insert(ExampleModel)

    @ferris3.auto_method(name="get_by_title", returns=SimpleListMessage)
    def get_by_title(self, request):
        db = MySQLdb.connect(host='127.0.0.1', user='root', db='test')
        cursor = db.cursor()
        cursor.execute('SELECT correo FROM user')
        data = []
        list_message = SimpleListMessage()
        for row in cursor.fetchall():
            data.append(SimpleModelMessage(simple=row[0]))

        db.close()

        list_message.items = data
        return list_message
