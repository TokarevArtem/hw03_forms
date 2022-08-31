import datetime


def year(request):
    year = datetime.datetime.today().year
    return {
        'year': year
    }
