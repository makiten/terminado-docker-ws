import configparser as cp
import re
import tornado.web
from tornado.ioloop import IOLoop
from terminado import TermSocket, SingleTermManager

config = cp.ConfigParser()
config.read('ws.cfg')
domain_re = config['domain']['pattern']


class JogralDomainTermSocket(TermSocket):
    def check_origin(self, origin):
        return bool(re.match(r'' + domain_re, origin))


if __name__ == '__main__':
    term_manager = SingleTermManager(shell_command=['bash'])
    handlers = [
        (r"/ws", JogralDomainTermSocket, {'term_manager': term_manager}),
    ]
    app = tornado.web.Application(handlers)
    app.listen(8000)
    try:
        IOLoop.current().start()
    except KeyboardInterrupt:
        pass
    finally:
        term_manager.shutdown()
        print("\n")
