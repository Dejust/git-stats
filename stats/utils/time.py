import tzlocal
import pytz
import datetime


def build_utc_datetime_from_timestamp(seconds):
    """
    Конвертирует количество секунд с 1970 года (в локальной таймзоне) 
    в datetime в таймзоне UTC
    :param: seconds - количество секунд с 1970 в локальной таймзоне
    """
    naive_datetime = datetime.datetime.fromtimestamp(seconds)
    local_datetime = tzlocal.get_localzone().localize(naive_datetime)
    return local_datetime.astimezone(pytz.UTC)

def utcnow():
    """
    Возвращает текущее время в UTC с установленной таймзоной
    """
    return datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

def format_utc(dt):
    """
    Форматирует UTC дату и время в строку
    """
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')
