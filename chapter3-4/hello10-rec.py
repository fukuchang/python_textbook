#無名関数を定義
def say_hello(i):
    if i <= 0:
        return
    print("hello", i)
    say_hello(i-1)
#実行
say_hello(10)
