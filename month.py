import Tex

class Month:
    MONTH_NAMES=["Januari", "Februari", "Mars",
                 "April", "Maj", "Juni",
                 "Juli", "Augusti", "September",
                 "Oktober", "November", "December"]
    def __init__(self, index, image):
        self.index = index
        self.image = image
        print "hello, month"

    def make_image(self, image, desc, date):
        Tex.create_image_tex(image, desc, date)

    def make_month_name(self, index):
        Tex.create_month_name_tex(Month.MONTH_NAMES[index])

    def make_days(self, index):
        Tex.create_days_tex()

    def make_month(self, index, image):
        self.make_image(image, "", "")
        self.make_month_name(index)
        self.make_days(index)
        print "month", index
