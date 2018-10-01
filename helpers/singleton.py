

class Singleton(type):
    instance = None

    def __init__(cls, name, bases, dict):
        cls._type = type(name, bases, dict)

    def __call__(mcs, *a, **kw):
        if not mcs.instance:
            mcs.instance = mcs._type(*a, **kw)
        return mcs.instance
