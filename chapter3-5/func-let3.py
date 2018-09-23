 #引数に関数を要求する関数を定義
def calc_5_3(func):
    return func(5, 3)

#引数に関数を指定する
result = calc_5_3(lambda a,b: a * b)
print(result)

result = calc_5_3(lambda a,b: a + b)
print(result)
