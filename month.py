from tex import Tex
import datetime
from calendar import monthrange

class Month:
    MONTH_NAMES=["Januari", "Februari", "Mars",
                 "April", "Maj", "Juni",
                 "Juli", "Augusti", "September",
                 "Oktober", "November", "December"]
    def __init__(self, year, month, image):
        self.year = year
        self.month = month
        self.image = image

    def make_image(self, desc, date):
        Tex.create_image_tex(self.image, desc, date)

    def make_month_name(self):
        Tex.create_month_name_tex(Month.MONTH_NAMES[self.month-1])

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
        self.make_image("desc", "date")
        self.make_month_name()
        self.make_days()
        Tex.finalize(self.month)
