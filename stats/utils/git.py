from datetime import datetime

from git import Repo
from django.conf import settings

from stats.utils import time


def get_repo_stats():
    repo = Repo(settings.BASE_DIR) 

    head_commit = repo.head.commit
    active_branch = repo.active_branch
    commited_date = time.build_utc_datetime_from_timestamp(repo.head.commit.committed_date)
    tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)

    return {
        'commit': head_commit.hexsha,
        'branch': active_branch.name,
        'commit_date': time.format_utc(commited_date),
        'version': tags[-1].name if tags else None
    }
