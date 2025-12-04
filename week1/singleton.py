class Singleton:  # Using static method
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        try:
            if Singleton.__instance != None:
                raise Exception("This class is a singleton!")
            else:
                Singleton.__instance = self
        except Exception as e:
            print(e)
        else:
            print("Here is your instance..")
        finally:
            pass


class SingletonNew:  # Using __new__
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


def singleton(cls):  # Using Decorator
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class Logger:
    def __init__(self):
        self.msg = "Logging Started"

    def show(self):
        print(self.msg)


class SingletonMeta(type):  # Using Metaclass
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.name = "Main DB"


print("\n---- Using static method ----")
s1 = Singleton.getInstance()
print(s1)
s2 = Singleton.getInstance()
print(s2)
s3 = Singleton()
print(s3)


print("\n---- Using __new__ ----")
a = SingletonNew()
print(a)
b = SingletonNew()
print(b)
print("Singleton (__new__):", a is b)

print("\n---- Using Decorator ----")
l1 = Logger()
print(l1)
l1.show()
l2 = Logger()
print(l2)
l2.show()
print("Decorator Singleton:", l1 is l2)

print("\n---- Using Metaclass ----")
d1 = Database()
print(d1)
d2 = Database()
print(d2)
print("Metaclass Singleton:", d1 is d2)
