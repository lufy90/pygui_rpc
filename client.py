import xmlrpc.client
import pickle


class Client():
    def __init__(self, server):
        self.proxy = xmlrpc.client.ServerProxy(server)

    def run(self, func, *a, **kw):
        ret = getattr(self.proxy, func)(*a,**kw)
        if ret['status'] == 'success':
            return pickle.loads(ret['data'].data)
        else:
            raise Exception('rpc failed: ' + pickle.loads(ret['data'].data))

if __name__ == '__main__':
    client = Client('http://localhost:8006')

    ## move mouse to coordinate (10,20)
    ret = client.run('moveTo', 10, 20)
