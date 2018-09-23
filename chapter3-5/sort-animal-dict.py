#(動物．最高時速)のリスト(各要素はタプルで作成)
animal_dict = {
    "ライオン": 58,
    "チーター": 110,
    "シマウマ": 60,
    "トナカイ": 80,
}

#足の早い順に並び替える
li = sorted(
    animal_dict.items(),
    key = lambda x : x[1],
    reverse = True
)

#結果を表示
for name,speed in li: print(name, speed)
