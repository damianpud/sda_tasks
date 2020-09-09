import time


def interval(value):
    def delay(*args, **kwargs):
        time.sleep(5)
        return value(*args, **kwargs)
    return delay


@interval
def multiply(first, second):
    return first * second


first = 10
second = 20

if __name__ == '__main__':
    print(multiply(first, second))  # == interval(multiply)(a,b)
