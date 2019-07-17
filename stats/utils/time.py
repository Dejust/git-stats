import tzlocal
import pytz
import datetime


def build_utc_datetime_from_timestamp(seconds):
    """
    Возвращает DATETIME в таймзоне UTC
    :param: seconds - количество секунд с 1970 в локальной таймзоне
    """
    naive_datetime = datetime.datetime.fromtimestamp(seconds)
    local_datetime = tzlocal.get_localzone().localize(naive_datetime)
    return local_datetime.astimezone(pytz.UTC)

def utcnow():
    return datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

def format_utc(dt):
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')
