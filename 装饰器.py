import functools
import time

# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper

# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args,**kw):
#             print('%s %s():' %(text,func.__name__))
#             return func(*args,**kw)
#         return wrapper
#     return decorator


def metric(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        start_time = time.time()
        f = func(*args,**kw)
        print('%s executed %s ms' % (func.__name__,time.time()-start_time))
        return func
    return  wrapper


@metric
def now():

    for i in range(10):
        i=i+1
    # time.sleep(3)
    print(i)

if __name__=='__main__':
    # now()
    # print(now.__name__)
    now()