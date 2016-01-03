class Tex:
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
        #create_image_tex

    @staticmethod
    def create_month_name_tex(name):
        #create_month_name_tex

    @staticmethod
    def create_days_tex():
        #create_days_tex
