def timer(func):
    def wrapper(*args, **kwargs):
        import time

        start = time.time()
        res = func(*args, **kwargs)
        print(f"耗时：{time.time() - start:.2f}s")
        return res

    return wrapper


# @timer 等价于 test = timer(test)
@timer
def test():
    sum(range(1000000))


if __name__ == "__main__":
    test()
