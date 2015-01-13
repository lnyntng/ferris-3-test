from google.appengine.ext import ndb, db
from ferris3 import Model, Service, hvild, auto_service
import ferris3 as f3
from pprint import pprint

from app.custom_properties.translations import *
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


@auto_service
class ProgramsService(Service):
    list = hvild.list(Program)
    get = hvild.get(Program)
    delete = hvild.delete(Program)
    insert = hvild.insert(Program)
    update = hvild.update(Program)
