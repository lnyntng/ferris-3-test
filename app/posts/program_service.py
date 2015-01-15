import ferris3 as f3
import protopigeon
import logging

from google.appengine.ext import ndb, db
from ferris3 import Model, Service, hvild, auto_service
from ferris3.translations import StringTranslationProperty, TextTranslationProperty, ChoiceTranslationProperty
from protorpc import messages

from app.choices_presets.common_choices import *
from app.choices_presets.program_choices import *


class Program(Model):
    name = ndb.StringProperty(required=True)
    type = ChoiceTranslationProperty(required=True, choices=PROGRAM_TYPES)
    description = ndb.TextProperty(required=True)
    duration = ndb.StringProperty()
    picture = ndb.StringProperty()
    audience = ChoiceTranslationProperty(choices=LEVELS_OF_EDUCATION, repeated=True)
    delivery_method = ChoiceTranslationProperty(choices=DELIVERY_METHODS)
    minimum_capacity = ndb.IntegerProperty()
    maximum_capacity = ndb.IntegerProperty()
    languages = ChoiceTranslationProperty(choices=LANGUAGES, repeated=True)
    tags = ndb.StringProperty(repeated=True)
    currency_type = ndb.StringProperty(choices=CURRENCY_CHOICES)
    amount = ndb.FloatProperty()
    description_cost = ndb.StringProperty()
    is_default = ndb.BooleanProperty(default=False)
    item_language = ChoiceTranslationProperty(choices=LANGUAGES)
    string_test = StringTranslationProperty()
    text_test = TextTranslationProperty()

    def before_put(self):
        pass

    def set_key_name(self, keyname):
        self.key = ndb.Key(Program, keyname)


class KeynameMessage(messages.Message):
    keyname = messages.StringField(1, required=True)


ProgramMessage = f3.model_message(Program)
ProgramWithKeynameMessage = protopigeon.compose(ProgramMessage, KeynameMessage)
ProgramListMessage = f3.list_message(ProgramMessage)


@auto_service
class ProgramsService(Service):
    get = hvild.get(Program)
    list = hvild.list(Program)
    delete = hvild.delete(Program)
    insert = hvild.insert_with_keyname(Program)
    update = hvild.update(Program)
