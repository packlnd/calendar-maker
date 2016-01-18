# -*- coding: utf-8 -*-
from month import Month
from tex import Tex
import os

class TexCalendar:
    def __init__(self, year, images):
        self.year = int(year)
        self.images = images

    def help_stitch(self, a, b, c):
        os.system(
            "pdfunite pdfs/%s.pdf pdfs/%s.pdf pdfs/%s.pdf" %
            (a,b,c))

    def stitch(self):
        self.help_stitch("a", "b", "p")
        self.help_stitch("p", "c", "q")
        self.help_stitch("q", "d", "r")
        self.help_stitch("r", "e", "s")
        self.help_stitch("s", "f", "t")
        self.help_stitch("t", "g", "u")
        self.help_stitch("u", "h", "v")
        self.help_stitch("v", "i", "w")
        self.help_stitch("w", "j", "x")
        self.help_stitch("x", "k", "y")
        self.help_stitch("y", "l", "../calendar")
        os.system("rm -r pdfs calendar.aux calendar.log")

    def make_pdf(self):
        for i in range(12):
            Month(self.year, i+1, self.images[i]).make()
        self.stitch()

    #def add_holiday(self):
    #    print "holiday"

    #def add_birthday(self):
    #    print "birthday"

#t = TexCalendar(2016, [
#    ("sunrise.jpg", "Soluppgång, Fuengirola, Spanien", "9 juli 2015"),
#    ("ggb.jpg", "Soluppgång över Golden Gate-bron, San Francisco, Kalifornien", "28 november 2015"),
#    ("Amsterdam.jpg", "Kanal, Amsterdam", "26 juli 2015"),
#    ("homecoming.jpg", "Husky Stadium, Seattle, Washington", "17 oktober 2015"),
#    ("kerrypark.jpg", "Kerry Park, Seattle, Washington", "21 november 2015"),
#    ("lightshow.jpg", "Gas Works Park, Seattle, Washington", ""),
#    ("oregonstate.jpg", "Reeser Stadium, Corvallis, Oregon", "21 november 2015"),
#    ("sensoji.jpg", "Sensoji-templet, Tokyo, Japan", "19 december 2015"),
#    ("snoqualmie.jpg", "Snoqualmie Falls, Snoqualmie, Washington", ""),
#    ("spaceneedle.jpg", "desc", "date"),
#    ("Town.jpg", "Utsikt från balkongen, Fuengirola, Spanien", ""),
#    ("BigBen.jpg", "Big Ben, London", "18 juli 2015")
#])
##t.add_birthday(2,7,"My birthday")
#t.make_pdf()
