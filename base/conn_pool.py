# -*- coding=utf-8 -*-


class ConnPool():
    """
    @author heshipeng
    tcp连接池
    """
    def __init__(self):
        """
        初始化数据结构
        """
        self.conn_instances = dict()
        self.conn_keys = set()

    def put(self, key, value):
        self.conn_keys.add(key)
        self.conn_instances[key] = value

    def get(self, key):
        if self.conn_keys.__contains__(key):
            return self.conn_instances.get(key)
        else:
            raise Exception("Key not exist")

    def keys(self):
        return self.conn_keys

    def items(self):
        result = set()
        if self.conn_instances:
            for conn in self.conn_instances:
                result.add(conn)

        return result