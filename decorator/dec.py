'''
http://blog.jkey.lu/2013/03/15/python-decorator-and-functools-module/
'''


def dec_wrapper(name):
    print "in dec wrapper name = %s" % name
    def f(func):
        def wrapper(*arg):
            print "in wrapper"
            return func(*arg)
        return wrapper
    return f


@dec_wrapper("example")
def sum(x, y):
    return x + y


print sum(100,1000)
