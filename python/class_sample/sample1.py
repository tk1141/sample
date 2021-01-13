#! python3

class Spam1:
    val = 100

    def ham(self):
        self.egg('call method')

    def egg(self, msg):
        print("{0}".format(msg))
        print('val:{}'.format(self.val))


class Spam2:
    # コンストラクタ
    def __init__(self, ham, egg):
        self.ham = ham
        self.egg = egg

    def output(self):
        sum = self.ham + self.egg
        print("{0}".format(sum))


spam1 = Spam1()
spam1.ham()

spam2 = Spam2(5, 10)
spam2.output()
