# -*- coding=utf-8 -*-


from peewee import *

db = SqliteDatabase('chat.db')


class User(Model):
    """
     @author heshipeng
     用户信息表
    """

    id = PrimaryKeyField(11)
    uni_uuid = CharField(40)
    username = CharField(70)
    password = CharField(40)
    nickname = CharField(70)
    status = IntegerField(1)
    create_time = BigIntegerField(20)
    update_time = BigIntegerField(20)
    last_login_time = BigIntegerField(20)

    class Meta:
        database = db


class Message(Model):

    """
    @author heshipeng
    用户消息表
    """

    id = PrimaryKeyField(11)
    user_uuid = CharField(40)
    message = TextField()
    status = IntegerField(1)
    create_time = BigIntegerField(20)
    update_time = BigIntegerField(20)

    class Meta:
        database = db


class ChatPool(Model):

    """
    @author heshipeng
    服务连接表
    """

    id = PrimaryKeyField(11)
    uni_uuid = CharField(40)
    username = CharField(70)
    address = CharField(70)
    status = IntegerField(1)
    create_time = BigIntegerField(20)
    update_time = BigIntegerField(20)

    class Meta:
        database = db


class Group(Model):

    """
    @author heshipeng
    群组表
    """

    id = PrimaryKeyField(11)
    uni_uuid = CharField(40)
    member_size = IntegerField(6)
    max_size = IntegerField(6)
    create_time = BigIntegerField(20)
    update_time = BigIntegerField(20)

    class Meta:
        database = db


class GroupMember(Model):

    """
    @author heshipeng
    群成员表
    """

    id = PrimaryKeyField(11)
    user_uuid = CharField(40)
    group_uuid = CharField(40)
    create_time = BigIntegerField(20)
    update_time = BigIntegerField(20)

    class Meta:
        database = db


if __name__ == '__main__':
    db.connect()
    db.create_tables([User, Message, ChatPool, Group, GroupMember])