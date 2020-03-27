from peewee import *
from .model_base import BaseModel
from . import db


class Server(BaseModel):
    id = PrimaryKeyField()
    name = CharField(default='')
    host = CharField(null=False)
    online = IntegerField(default=-1, null=True)
    version = CharField(default='')
    ping = DoubleField(default=-1)

    def keys(self):
        return 'id', 'name', 'host', 'online', 'version', 'ping', 'update_timestamp'

    class Meta:
        database = db
