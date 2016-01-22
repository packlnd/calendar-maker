# -*- coding: utf-8 -*-
from month import Month
from tex import Tex
import os

class TexCalendar:
    def __init__(self, year, images, lang):
        self.year = int(year)
        self.images = images
        self.lang = lang

    def help_stitch(self, a, b, c):
        print "Stitching....",
        os.system("pdfunite pdfs/%s.pdf pdfs/%s.pdf pdfs/%s.pdf" % (a,b,c))
        print "Done"

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
        self.help_stitch("y", "l", "../static/calendar")
        os.system("rm -r pdfs calendar.aux calendar.log")

    def make_month(self,i):
        print "Making month:",i,"....",
        Month(self.year, i, self.images[i-1], self.lang).make()
        print "Done"
