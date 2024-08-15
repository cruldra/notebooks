from peewee import *

database = MySQLDatabase('hichat', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': '192.168.1.4', 'user': 'root', 'password': '123394'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class HiUser(BaseModel):
    anonymous = IntegerField(constraints=[SQL('DEFAULT 0')])
    avatar = CharField(null=True)
    creation_time = DateTimeField(null=True)
    is_internal_employee = IntegerField(constraints=[SQL('DEFAULT 0')])
    password = CharField(null=True)
    pen_name = CharField(null=True)
    update_time = DateTimeField(null=True)
    username = CharField(unique=True)
    version = IntegerField(constraints=[SQL('DEFAULT 0')])

    class Meta:
        table_name = 'hi_user'

class HiFile(BaseModel):
    content_type = CharField(null=True)
    creation_time = DateTimeField(null=True)
    full_name = CharField(null=True)
    meta = TextField(null=True)
    purpose = CharField(null=True)
    simple_name = CharField(null=True)
    size = IntegerField(null=True)
    update_time = DateTimeField(null=True)
    url = TextField(null=True)
    user = ForeignKeyField(column_name='user_id', field='id', model=HiUser, null=True)
    version = IntegerField(constraints=[SQL('DEFAULT 0')])

    class Meta:
        table_name = 'hi_file'

