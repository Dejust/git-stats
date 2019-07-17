## Установка и запуск

```bash
git clone git@github.com:Dejust/git-stats.git
cd git-stats
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

## API

Получить информацию о приложении

```
GET /stats/fetch
```

```json
{
    "commit": "aad95f46b5ee6abcd99c3a165aa20297642d38ec",  // хеш хед-коммита текущей ветки
    "commit_date": "2018-04-12T07:53:19Z",  // дата хед-коммита текущей ветки
    "branch": "feature/adding_status_info", // текущая ветка
    "version": "release_v1.16.1", // максимальный тег хед-коммита
    "started": "2018-04-12T09:33:25Z", // дата и время запуска приложения
    "uptime_seconds": 69470 // количество секунд между текущим временем на момент запроса и started
}
```