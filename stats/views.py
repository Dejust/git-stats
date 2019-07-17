from django.shortcuts import render
from django.http import JsonResponse

from stats.utils import git

def fetch_app_stats(request):
    """
    Возвращает текущую информацию о репозитории приложения и времени его запуска
    """
    stats = git.get_repo_stats()
    return JsonResponse(stats)