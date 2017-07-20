#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/7/16 16:34
# @Author  : otfsenter
# @File    : aiodemo.py.py

# pip install aiopeewee

from aiopeewee import AioModel, AioMySQLDatabase
from peewee import CharField, TextField, DateTimeField, IntegerField
from peewee import ForeignKeyField, PrimaryKeyField
from aiopeewee import model_to_dict

import asyncio

loop = asyncio.get_event_loop()


db = AioMySQLDatabase('test', host='127.0.0.1', port=3306,
                     user='root', password='spwx')


async def db_connect():
    await db.connect(loop)


async def db_close():
    await db.close()


class User(AioModel):
    username = CharField()

    class Meta:
        database = db


class Blog(AioModel):
    user_id = IntegerField()
    title = CharField(max_length=25)
    content = TextField(default='')
    pub_date = DateTimeField(null=True)
    pk = PrimaryKeyField()

    class Meta:
        database = db


async def demo():

    # create connection pool

    # count
    count = await User.select().count()

    # async iteration on select query
    # async for user in User.select():
    #     print(user)
    #
    # # fetch all records as a list from a query in one pass
    # users = await User.select()
    # print((users))
    # # serialized = await model_to_dict(users)
    # # print(serialized)

    # user = await User.create(username='kszucs')
    # user = await User.create(username='kszucs')
    # user = await User.create(username='kszucs')
    # user = await User.create(username='kszucs')
    # user = await User.create(username='kszucs')
    # user = await User.create(username='kszucs')
    # user = await User.create(username='kszucs')
    # user = await User.create(username='kszucs')
    # user = await User.create(username='kszucs')
    user = await User.create(username='kszucs')

    # # modify
    user.username = 'krisztian'
    await user.save()

    users = await User.select().dicts()

    # insert

    # serialized = await model_to_dict(user)

    serialized = None

    return [users, count, serialized]

    # async iteration on blog set
    # [b.title async for b in user.blog_set.order_by(Blog.title)]

    # close connection pool

    # see more in the tests

class BusinessError(Exception):
    pass

async def atomic_demo():
    for i in range(3):
        await User.create(username=f'u{i}')

    try:
        async with db.atomic():
            user = await User.get(User.username == 'u1')
            await user.delete_instance()
            user = await User.get(User.username == 'u2')
            await user.delete_instance()

            raise Exception()
    except:
        pass

    usernames = [u.username async for u in User.select()]
    return usernames


# tasks = [demo()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()