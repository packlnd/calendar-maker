from month import Month

class Image:
    def __init__(self, img, desc, date, i):
        self.fname='tmp'+str(i)
        img.save('./images/' + self.fname)
        self.fname=img.filename
        self.date=date
        self.desc=desc

class Data:
    def __init__(self, lang, start_day, year, images):
        self.lang=lang
        self.start_day=start_day
        self.year=year
        self.images=images

class Util:
    @staticmethod
    def extract_form_images(fs,fm):
        res=[]
        for i,m in enumerate(Month.SHORT_NAMES):
            res.append(Image(fs['browse-'+m], fm['desc-'+m], fm['date-'+m],i))
        return res

    @staticmethod
    def extract_form_data(fm,fs):
        return Data(fm['lang'],
                fm['start_of_week'],
                fm['year'],
                Util.extract_form_images(fs,fm))

    @staticmethod
    def validate_data(fm, fs):
        form_data=['lang','start_of_week','year']
        file_data=[]
        for i in ('desc','date'):
            for m in Month.SHORT_NAMES:
                form_data.append(i+"-"+m)
                file_data.append('browse-'+m)
        for d in form_data:
            if not d in fm:
                print d,"does not exist"
                return False
        for d in file_data:
            if not d in fs:
                print d,"does not exist"
                return False
        return True
