#オリジナルデータ
class BMI:
    def __init__(self):
        self.weight = 0
        self.height = 0
        self.bmi = 0

    def setData(self, weight, height):
        self.weight = weight
        self.height = height / 100
        self.bmi = self.weight / (self.height * self.height)

    def judgeBMI(self):
        if self.bmi < 18.5:
            return "痩せ型"
        if (18.5 <= self.bmi) and (self.bmi < 25):
            return "標準体重"
        if (25 <= self.bmi) and (self.bmi < 30):
            return "肥満(軽)"
        if self.bmi >= 30:
            return "肥満(重)"

human1 = BMI()
human1.setData(68, 160)
print(human1.judgeBMI())
