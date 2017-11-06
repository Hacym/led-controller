import os

from peewee import *

from config import get_config

config = get_config()

db = SqliteDatabase(os.path.expanduser(config.get('database', 'location')))

class BaseModel(Model):
    class Meta:
        database = db

class Strip(BaseModel):
    strip_id = IntegerField(primary_key=True)
    name = CharField()
    length = IntegerField()

class LED(BaseModel):
    led_id = IntegerField(primary_key=True)
    strip_id = ForeignKeyField(Strip, null=True)
    position = IntegerField()
    r = IntegerField()
    g = IntegerField()
    b = IntegerField()
    on = BooleanField(default=True)

if __name__ == "__main__":
    db.create_tables([Strip, LED])
