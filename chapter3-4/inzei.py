#印税を計算する関数
def calc_royality(price, sales, per):
    rate = per / 100
    ro = int(price * sales * rate)
    return ro

#ユーザから情報を入力してもらう
i = input("定価は？")
price = int(i)

i = input("発行部数は？")
sales = int(i)

i = input("印税率(パーセント)は？")
per = int(i)

#結果を表示する
v = calc_royality(price, sales, per)
print("印税は",v,"円です")
