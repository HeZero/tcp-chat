from base.server import BaseServer

if __name__ == '__main__':
    server = BaseServer()
    print('请输入：')
    msg = input()
    server.broadcast(msg)
