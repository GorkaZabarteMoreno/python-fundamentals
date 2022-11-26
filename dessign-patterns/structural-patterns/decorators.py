from os.path import abspath
from json import dumps


def log(method):
    def wrapper(*args, **kwargs):
        with open('app.log', 'a') as f:
            path = abspath('')
            try:
                method(*args, **kwargs)
                status = 0
            except Exception:
                status = 1

            log_ = {
                'file': path, 
                'function': method.__name__,
                'status': 0 if status == 0 else 1
                    }
            f.write(dumps(log_))
    return wrapper


@log
def func(x: float, y: float) -> float:
    try:
        res = x / y
    except ZeroDivisionError:
        raise ZeroDivisionError('Division by 0')
    return res


if __name__ == '__main__':
    func(2, 1)
    func(2, 0)
