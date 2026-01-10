class BMI:
    def __init__(self):
        self.__height = 0
        self.__weight = 0
        self.__bmi = 1
    def set_weight(self, weight):
        self.__weight = weight
    def set_height(self, height):
        self.__height = height
    def cal_bmi(self):
        self.__bmi = self.__weight / (self.__height * self.__height)
    def display_BMI(self):
        self.cal_bmi()
        return self.__bmi

satyam = BMI()
satyam.set_height(1.68)
satyam.set_weight(76)
print(satyam.display_BMI())