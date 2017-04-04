import tornado.web
from tornado.ioloop import IOLoop
from terminado import TermSocket, SingleTermManager

if __name__ == '__main__':
    term_manager = SingleTermManager(shell_command=['bash'])
    handlers = [
        (r"/ws", TermSocket, {'term_manager': term_manager}),
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
