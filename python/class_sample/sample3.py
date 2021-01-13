#! python3

class Spam:
    # private
    __attr = 100

    def __init__(self):
        self.__attr = 999

    def method(self):
        self.__methond()

    # private
    def __methond(self):
        print(self.__attr)


spam1 = Spam()
spam1.method()
