from django.shortcuts import render
from django.http import JsonResponse

from stats.utils import git, uptime

def fetch_app_stats(request):
    """
    Возвращает текущую информацию о репозитории приложения и времени его запуска
    """
    git_stats = git.get_repo_stats()
    uptime_stats = uptime.get_uptime_stats()
    return JsonResponse(dict(git_stats.items() | uptime_stats.items()))