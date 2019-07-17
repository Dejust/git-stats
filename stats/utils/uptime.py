import pytz
import os
import psutil

from stats.utils import time


def get_uptime_stats():
    """Возвращает UPTIME текущего процесса"""
    current_pid = os.getpid()
    current_process = psutil.Process(current_pid)
    start_at = time.build_utc_datetime_from_timestamp(current_process.create_time())
    now = time.utcnow()
    return {
        'started': time.format_utc(start_at),
        'uptime_seconds': int((now - start_at).total_seconds())
    }