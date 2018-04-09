# -*- coding=utf-8 -*-

import uuid
import hashlib
import time
from base.server import BaseClient
from base.chat_model import *
from common.response import ChatResponse, api_code


class ChatClient(BaseClient):

    def __init__(self):
        super.__init__()
        db.connect()
        self.recv()

    def register(self, username, nickname, password):
        # 两次md5加密
        pwd = hashlib.md5(hashlib.md5(password))
        now = time.time()
        user = User(uni_uuid=uuid.uuid1(), username=username, password=pwd, nickname=nickname,
                    create_time=now, update_time=0, last_login_time=now)
        if user.save() > 0:
            return ChatResponse(user)
        else:
            return ChatResponse(code=api_code['server_error'], message="register fail")

    def login(self, username, password):
        self.connect()
        user = User.select().where(User.username == username).get()
        if user:
            pwd = hashlib.md5(hashlib.md5(password))
            if user.password == pwd:
                self.connect()
                now = time.time()
                User.update(User.last_login_time == now, User.update_time == now).where(User.username == username)

            else:
                return ChatResponse(code=api_code['param_error'], message='password error')
        else:
            return ChatResponse(code=api_code['server_error'], message='user not exist')