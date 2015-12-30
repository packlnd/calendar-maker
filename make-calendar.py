class TexCalendar:
    def __init__(self, year, images):
        self.year = year
        self.images = images
        print "hello, world"

    def make_pdf(self):
        print "make"

    def add_holiday(self):
        print "holiday"

TexCalendar(2016, [
    "fuengirola.jpg",
    "golden-gate.jpg",
    "senso-ji.jpg",
    "kerry.jpg"
]).make_pdf()
