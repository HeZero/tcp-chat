# -*- coding=utf-8 -*-


import socket
from base.conn_pool import ConnPool
from threading import Thread


class BaseServer():

    max_wait_con = 5

    def __init__(self, host="127.0.0.1", port=2223):
        self.sk = socket.socket()
        self.sk.bind((host, port))
        self.conn_pool = ConnPool()
        th = Thread(target=self.start_listen, args=())
        th.start()

    def start_listen(self, max_wait=max_wait_con):
        self.sk.listen(max_wait)
        while True:
            conn, address = self.sk.accept()
            self.conn_pool.put(address, conn)

    def get_conn_by_address(self, address):
        return self.conn_pool.get(address)

    def get_all_conn(self):
        return self.conn_pool.items()

    def send(self, address, msg):
        conn = self.get_conn_by_address(address)
        if not conn:
            raise Exception('disconnect from the client')
        else:
            if isinstance(msg, bytes):
                conn.send(msg)
            else:
                conn.send(bytes(msg, encoding="utf-8"))

    def sendall(self, address, msg):
        conn = self.get_conn_by_address(address)
        if not conn:
            raise Exception('disconnect from the client')
        else:
            if isinstance(msg, bytes):
                conn.sendall(msg)
            else:
                conn.sendall(bytes(msg, encoding="utf-8"))

    def broadcast(self, msg):
        for address in self.conn_pool.keys():
            self.sendall(address, msg)


class BaseClient():

    def __init__(self):
        self.isConnect = False
        self.client = socket.socket()

    def connect(self, host="127.0.0.1", port=2223):
        address = (host, port)
        self.client.connect(address)
        self.isConnect = True
        th = Thread(target=self.recv, args=())
        th.start()
        return self.client

    def recv(self):
        try:
            ret = str(self.client.recv(1024), encoding="utf-8")
            return ret
        except Exception as e:
            print(e)
            raise Exception('Lost connection to remote server')

    def send(self, msg):
        if self.isConnect:
            if isinstance(msg, bytes):
                self.client.send(msg)
            else:
                self.client.send(bytes(msg, encoding="utf-8"))
        else:
            raise Exception("client is not connected remote server")
