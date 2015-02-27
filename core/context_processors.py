import datetime

def countrytimes(request):
    local = datetime.datetime.now()
    return {
        'local':local,
    }