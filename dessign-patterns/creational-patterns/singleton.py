class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


class Logger(Singleton):

    instance = None

    def __init__(self, path_logfile: str = '../app.log'):
        self.path = path_logfile
