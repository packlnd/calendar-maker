class Tex:
    MONTH_NAMES=["Januari", "Februari", "Mars",
                 "April", "Maj", "Juni",
                 "Juli", "Augusti", "September",
                 "Oktober", "November", "December"]
    TEX_NAMES=["jan","feb","mar","apr","maj","jun",
               "jul","aug","sep","okt","nov","dec"]
    IMAGE_STRING = \
        "\noindent\includegraphics[scale=0.7425]{%s}\\" + \
        "\textit{\textsc{%s}}\hfill\textit{\textsc{%s}}"
    MONTH_NAME_STRING = \
        "\Huge{\textbf{%s}}"
    DAY = "\tb"
    OTHER_DAY = "\nd"
    OTHER_RED = "\ns"
    HOLIDAY = "\rd"

    @staticmethod
    def image_text(img, desc, date):
        return Tex.IMAGE_STRING % (img, desc, date)

    @staticmethod
    def name_string(name):
        return Tex.MONTH_NAME_STRING % name

    @staticmethod
    def create_image_tex(img, desc, date):
        Tex.write_to_file("image.tex",
                Tex.image_tex(img, desc, date))

    @staticmethod
    def create_month_name_tex(name):
        Tex.write_to_file("image.tex",
                Tex.name_string(name))

    @staticmethod
    def create_days_tex():
        #create_days_tex

    @staticmethod
    def write_to_file(fn, text):
        f = open(fn, 'w')
        f.write(text)
        f.close()
