from tex import Tex
import datetime
from calendar import monthrange
from util import Util

class Month:
    def __init__(self, year, month, img, lang):
        self.year = year
        self.month = month
        self.img = img
        self.MONTH_NAMES = Util.read_months(lang)
        self.WEEK_DAYS = Util.read_weekdays(lang)

    def make_image(self):
        Tex.create_image_tex(self.img.fname, self.img.desc, self.img.date)

    def make_month_name(self):
        Tex.create_month_name_tex(self.MONTH_NAMES[self.month-1])

    def make_weekday_names(self):
        Tex.create_weekday_name_tex(self.WEEK_DAYS)

    def get_days_in_prev_month(self, y, m):
        py = y
        pm = m-1
        if m is 1:
            py = y-1
            pm = 12
        return monthrange(py, pm)[1]

    def make_days(self):
        first_day_index = datetime.date(self.year, self.month, 1).weekday()
        print first_day_index
        days_in_month = monthrange(self.year, self.month)[1]
        days_prev_month = self.get_days_in_prev_month(self.year, self.month)
        Tex.create_days_tex(days_in_month, first_day_index,
                days_prev_month)

    def make(self):
        self.make_image()
        self.make_month_name()
        self.make_weekday_names()
        self.make_days()
        Tex.finalize(self.month)
