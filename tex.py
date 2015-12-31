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
