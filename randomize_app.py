import random
from statistics import mean


class RandomizeForColleage:
    __raiting = 0 #avg
    __numbers = 0 #count
    __IsBool = True
    __iterable = 0
    __array = []

    def __init__(self, values) -> None:
        self.__numbers = values[0]
        self.__raiting = values[1]
        self.__array.clear()
    
    def get_raiting(self):
        return self.__raiting
    
    def get_numbers(self):
        return self.__numbers

    def get_bool(self):
        return self.__IsBool
    
    def get_iter(self):
        return self.__iterable

    def __dispose_high_value(self):
        val = self.__raiting * self.__numbers / self.__numbers
        ret_val = 0

        for i in range(self.__numbers):
            rnd = random.randint(1, 7)
            self.__array.append(int(val - rnd))
            ret_val = ret_val + rnd

        iterable = 0
        while ret_val > 0:
            rnd = random.randint(1, 7)

            if(self.__array[iterable] + rnd) < 100:
                if ret_val - rnd < 0:
                    ret_val = ret_val * (-1)
                    self.__array[iterable] = self.__array[iterable] - ret_val
                    break

                self.__array[iterable] = self.__array[iterable] + rnd
                ret_val = ret_val - rnd

            iterable = iterable + 1

            if iterable >= self.__numbers:
                iterable = 0

    def __dispose_low_value(self):
        smally_values = []

        for i in range(0, len(self.__array)):
            if self.__array[i] < 50:
                smally_values.append(50 - self.__array[i])
                self.__array[i] = 50

        for i in range(0, len(smally_values)):
            for j in range(len(self.__array)):
                if self.__array[j] - smally_values[i] > 50 and smally_values[i] > 0:
                    self.__array[j] = self.__array[j] - smally_values[i]
                    smally_values[i] = 0
                    break

        print(smally_values)

    def __fully_array_set(self, some_value):
        if some_value == 100:
            for i in range(0, self.__numbers):
                self.__array.append(100)

        elif some_value == 50:
            for i in range(0, self.__numbers):
                self.__array.append(50)

        elif 75 <= some_value < 100:
            if self.__raiting >= 90:
                self.__dispose_high_value()
                return

            for i in range(0, self.__numbers):
                self.__array.append(random.randint(60, 100))

        elif 75 > some_value > 50:
            for i in range(0, self.__numbers):
                self.__array.append(random.randint(30, 100))

            self.__dispose_low_value() 


    def run(self):
        while self.__IsBool:
            self.__fully_array_set(self.__raiting)

            if round(mean(self.__array)) == self.__raiting:
                self.__iterable += 1
                self.__IsBool = False

                return self.__array

            self.__array.clear()