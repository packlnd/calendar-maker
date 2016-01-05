import Tex

class Month:
    def __init__(self, index, image):
        self.index = index
        self.image = image
        print "hello, month"

    def make_image(self, desc, date):
        Tex.create_image_tex(self.image, desc, date)

    def make_month_name(self):
        Tex.create_month_name_tex(Month.MONTH_NAMES[self.index])

    def make_days(self):
        Tex.create_days_tex()

    def make(self):
        self.make_image("", "")
        self.make_month_name()
        self.make_days()
        print "month", self.index
