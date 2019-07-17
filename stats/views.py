from django.shortcuts import render
from django.http import JsonResponse


def fetch_app_stats(request):
    """
    Возвращает текущую информацию о репозитории приложения и времени его запуска
    """
    return JsonResponse({
        "commit": "aad95f46b5ee6abcd99c3a165aa20297642d38ec",
        "commit_date": "2018-04-12T07:53:19Z",
        "branch": "feature/adding_status_info",
        "version": "release_v1.16.1",
        "started": "2018-04-12T09:33:25Z",
        "uptime_seconds": 69470
    })