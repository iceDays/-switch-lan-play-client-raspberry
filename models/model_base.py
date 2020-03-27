from peewee import IntegerField, Model
import time
from . import db


class BaseModel(Model):
    update_timestamp = IntegerField(default=int(time.time()))

    def save(self, *args, **kwargs):
        self.update_timestamp = int(time.time())
        return super().save(*args, **kwargs)

    def keys(self):
        return ()

    def __getitem__(self, item):
        return getattr(self, item)

    def dict(self):
        return dict(self)

    class Meta:
        database = db
