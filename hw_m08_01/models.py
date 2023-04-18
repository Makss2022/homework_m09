from mongoengine import *


class Authors(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Qoutes(Document):
    quote = StringField()
    author = ReferenceField(Authors)
    tags = ListField(StringField(max_length=50))
