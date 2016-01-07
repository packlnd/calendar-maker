# -*- coding: utf-8 -*-
from month import Month
from tex import Tex
import os

class TexCalendar:
    def __init__(self, year, images):
        self.year = year
        self.images = images

    def stitch(self):
        os.system("pdfunite pdfs/a.pdf pdfs/b.pdf pdfs/p.pdf")
        os.system("pdfunite pdfs/p.pdf pdfs/c.pdf pdfs/q.pdf")
        os.system("pdfunite pdfs/q.pdf pdfs/d.pdf pdfs/r.pdf")
        os.system("pdfunite pdfs/r.pdf pdfs/e.pdf pdfs/s.pdf")
        os.system("pdfunite pdfs/s.pdf pdfs/f.pdf pdfs/t.pdf")
        os.system("pdfunite pdfs/t.pdf pdfs/g.pdf pdfs/u.pdf")
        os.system("pdfunite pdfs/u.pdf pdfs/h.pdf pdfs/v.pdf")
        os.system("pdfunite pdfs/v.pdf pdfs/i.pdf pdfs/w.pdf")
        os.system("pdfunite pdfs/w.pdf pdfs/j.pdf pdfs/x.pdf")
        os.system("pdfunite pdfs/x.pdf pdfs/k.pdf pdfs/y.pdf")
        os.system("pdfunite pdfs/y.pdf pdfs/l.pdf calendar.pdf")
        os.system("rm -r pdfs")

    def make_pdf(self):
        for i in range(12):
            Month(self.year, i+1, self.images[i]).make()
        self.stitch()

    #def add_holiday(self):
    #    print "holiday"

    #def add_birthday(self):
    #    print "birthday"

t = TexCalendar(2016, [
     ("sunrise.jpg", "Soluppgång i Fuengirola", "9 juli 2015"),
     ("ggb.jpg", "Soluppgång över Golden Gate-bron", "28 november 2015"),
     ("Amsterdam.jpg", "", ""),
     ("homecoming.jpg", "", ""),
     ("kerrypark.jpg", "", ""),
     ("lightshow.jpg", "", ""),
     ("oregonstate.jpg", "", ""),
     ("sensoji.jpg", "", ""),
     ("snoqualmie.jpg", "", ""),
     ("spaceneedle.jpg", "", ""),
     ("Town.jpg", "", ""),
     ("BigBen.jpg", "", "")
])
#t.add_birthday(2,7,"My birthday")
t.make_pdf()
