import datetime

# funkcje pomocnicze
def get_current_time():
    return datetime.datetime.now()
def get_yesterday_date():
    yesterday = get_current_time()-datetime.timedelta(days=1)
    return yesterday.date()
def get_created_yesterdays(model):
    return model.objects.filter(created__date=get_yesterday_date())
def get_updated_yesterdays(model):
    return model.objects.filter(updated__date=get_yesterday_date())
