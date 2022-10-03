# err_raise.py

# 触发异常：我们可以使用raise语句 ,一旦触发，立刻终止代码运行
# raise [exceotion]

def functionName(level):
    if level < 1:
        # raise Exception("Invalid level ",level)
        pass


try:
    functionName(0)
except Exception:
    print(1, Exception)
else:
    print("oooo")

functionName(0)

class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')

