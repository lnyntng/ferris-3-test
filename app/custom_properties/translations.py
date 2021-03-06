from google.appengine.ext import ndb, db


class StringTranslation(ndb.Model):
    english = ndb.StringProperty()
    spanish = ndb.StringProperty()
    portuguese = ndb.StringProperty()


class TextTranslation(ndb.Model):
    english = ndb.TextProperty()
    spanish = ndb.TextProperty()
    portuguese = ndb.TextProperty()


class ChoiceTranslation(ndb.Model):
    keyname = ndb.StringProperty()
    english = ndb.StringProperty()
    spanish = ndb.StringProperty()
    portuguese = ndb.StringProperty()


class BlobKeyTranslation(ndb.Model):
    spanish = ndb.BlobKeyProperty()
    english = ndb.BlobKeyProperty()
    portuguese = ndb.BlobKeyProperty()


class StringTranslationProperty(ndb.StructuredProperty):
    def __init__(self, **kwds):
        super(StringTranslationProperty, self).__init__(StringTranslation, **kwds)


class TextTranslationProperty(ndb.StructuredProperty):
    def __init__(self, **kwds):
        super(TextTranslationProperty, self).__init__(TextTranslation, **kwds)


class ChoiceTranslationProperty(ndb.StructuredProperty):
    #   Definition: objectProperty = ChoiceTranslationProperty(sp_choices=('hola',...), en_choices=('hello',...),pt_choices=('ola',...))
    #   Initialization: object = Object(title = ChoiceTranslation(keyname= 'hello'))
    def __init__(self, choices=None, **kwds):
        self.choices = choices
        super(ChoiceTranslationProperty, self).__init__(ChoiceTranslation, **kwds)

    def _validate(self, value):
        if not value.keyname:
            if not self.exist_in_dictionary(self.choices, value.keyname):
                raise TypeError('The value %s is not a valid choice option, possible options are %s ' % (repr(value.keyname), repr(self.choices.keys())))

    def exist_in_dictionary(self, choices, searched_value):
        for key in choices.keys():
            if key == searched_value:
                return True
        return False

    def _to_base_type(self, value):
        english = None
        spanish = None
        portuguese = None
        try:
            english = self.choices[value.keyname]['english']
        except Exception:
            pass
        try:
            spanish = self.choices[value.keyname]['spanish']
        except Exception:
            pass
        try:
            portuguese = self.choices[value.keyname]['portuguese']
        except Exception:
            pass
        tmodel = ChoiceTranslation(keyname=value.keyname, english=english, spanish=spanish, portuguese=portuguese)
        return tmodel

    def __unicode__(self):
        return '%s' % (self)


class BlobKeyTranslationProperty(ndb.StructuredProperty):
    def __init__(self, **kwds):
        super(BlobKeyTranslationProperty, self).__init__(BlobKeyTranslation, **kwds)
