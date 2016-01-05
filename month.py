import Tex
import datetime
import calendar

class Month:
    def __init__(self, year, index, image):
        self.index = index
        self.image = image

    def make_image(self, desc, date):
        Tex.create_image_tex(self.image, desc, date)

    def make_month_name(self):
        Tex.create_month_name_tex(Month.MONTH_NAMES[self.index])

    def make_days(self):
        d = datetime.date(year, index+1, 1)
        print d
        print d.weekday()
        self.days = [Tex.DAY]*(6*7)
        print self.days
        Tex.create_days_tex(d.weekday())

    def make(self):
        self.make_image("", "")
        self.make_month_name()
        self.make_days()
