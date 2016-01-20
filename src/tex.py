import os

class Tex:
    TEX_NAMES=["a","b","c","d","e","f",
               "g","h","i","j","k","l"]
    IMAGE_STRING = \
        "\\noindent\includegraphics[scale=0.7425]{%s}\\\\" + \
        "\\textit{\\textsc{%s}}\hfill\\textit{\\textsc{%s}}"
    MONTH_NAME_STRING = \
        "\Huge{\\textbf{\\textsc{%s}}}"
    DAY = "\\tb{%s}&"
    OTHER_DAY = "\\nd{%s}&"
    OTHER_RED = "\\ns{%s}&"
    HOLIDAY = "\\rd{%s}&"

    @staticmethod
    def image_text(img, desc, date):
        return Tex.IMAGE_STRING % (img, desc, date)

    @staticmethod
    def name_string(name):
        return Tex.MONTH_NAME_STRING % name

    @staticmethod
    def create_image_tex(img, desc, date):
        Tex.write_to_file("tex/image.tex",
                Tex.image_text(img, desc, date))

    @staticmethod
    def create_month_name_tex(name):
        Tex.write_to_file("tex/month_name.tex",
                Tex.name_string(name))

    @staticmethod
    def create_days_tex(days_m, first_day, days_prev_m):
        count=1
        d_arr=['']*42
        for i in range(first_day):
            frmt = Tex.OTHER_DAY
            if count % 7 == 0:
                frmt = Tex.OTHER_RED
            d_arr[i] = frmt % (i + days_prev_m - first_day + 1)
            count +=1
        for i in range(days_m):
            d_arr[(i + first_day)] = Tex.DAY % (i+1)
            count +=1
        next_m=1
        for i in range(days_m+first_day, 42):
            frmt = Tex.OTHER_DAY
            if count % 7 == 0:
                frmt = Tex.OTHER_RED
            d_arr[i] = frmt % next_m
            count +=1
            next_m+=1
        offset=0
        for i in range(7, 43, 7):
            d_arr.insert(i+offset, '\\nl\n')
            offset+=1
        Tex.write_to_file("tex/days.tex",
                (''.join(d_arr)).replace('&\\nl', '\\nl'))

    @staticmethod
    def write_to_file(fn, text):
        f = open(fn, 'w')
        f.write(text)
        f.close()

    @staticmethod
    def finalize(i):
        os.system("mkdir pdfs")
        os.system("pdflatex tex/calendar.tex")
        os.system("mv calendar.pdf pdfs/%s.pdf" % Tex.TEX_NAMES[i-1])
        print "Calendar finalized"
