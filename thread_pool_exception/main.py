from multiprocessing.dummy import Pool


def func_raise():
    d = {}
    return d['nonexisted']


def func():
    return 99


if __name__ == '__main__':
    threads = Pool(2)
    ret1 = threads.apply_async(func)
    ret2 = threads.apply_async(func_raise)
    ret1.get()
    try:
        ret2.get()
    except KeyError:
        print "catch key error!!"

