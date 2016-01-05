import Month

class TexCalendar:
    def __init__(self, year, images):
        self.year = year
        self.images = images

    def stitch(self):
        print "stitch"

    def make_pdf(self):
        for i in range(12):
            Month(i, self.images[i]).make()
        self.stitch()

    #def add_holiday(self):
    #    print "holiday"

    #def add_birthday(self):
    #    print "birthday"

t = TexCalendar(2016, [
    "fuengirola.jpg",
    "golden-gate.jpg",
    "senso-ji.jpg",
    "kerry.jpg"
])
#t.add_birthday(2,7,"My birthday")
t.make_pdf()
