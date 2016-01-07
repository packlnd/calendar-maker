from month import Month
from tex import Tex

class TexCalendar:
    def __init__(self, year, images):
        self.year = year
        self.images = images

    def stitch(self):
        print "stitch"

    def make_pdf(self):
        for i in range(2):
            Month(self.year, i+1, self.images[i]).make()
        self.stitch()

    #def add_holiday(self):
    #    print "holiday"

    #def add_birthday(self):
    #    print "birthday"

t = TexCalendar(2016, [
     "sunrise.jpg",
     "ggb.jpg"
    #"fuengirola.jpg",
    #"golden-gate.jpg",
    #"senso-ji.jpg",
    #"kerry.jpg"
])
#t.add_birthday(2,7,"My birthday")
t.make_pdf()
