class Month:
    MONTH_NAMES=["Januari", "Februari", "Mars",
                 "April", "Maj", "Juni",
                 "Juli", "Augusti", "September",
                 "Oktober", "November", "December"]
    def __init__(self, index, image):
        self.index = index
        self.image = image
        print "hello, month"

    def make_image(self, image):
        print "make image"

    def make_month_name(self, index):
        print "make month name"

    def make_days(self, index):
        print "make days"

    def make_month(self, index, image):
        self.make_image(image)
        self.make_month_name(index)
        self.make_days(index)
        print "month", index
