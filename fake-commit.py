# -*- coding: utf-8 -*-

import github3
from datetime import *
import time

gh = None


class Github:
    user_name      = "<github-user-name>"
    user_passwd    = "<password>"
    fake_repo_name = "fake-commit"


def has_commit_today():
    time_str = str(datetime.utcnow().date())
    print str(datetime.utcnow()), time_str
    print

    for repo in github3.iter_user_repos(Github.user_name):
        print repo.updated_at, repo.pushed_at, repo.name
        if time_str in str(repo.pushed_at):
            return True

    return False

def get_fake_repo():
    global gh

    repo = gh.repository(Github.user_name, Github.fake_repo_name)
    if repo:
        return repo
    else:
        return gh.create_repo(Github.fake_repo_name)

def fake_commit():
    repo = get_fake_repo()
    repo.create_file("./asd.md", "add asd.md", "asd")
    print repo


def main():
    global gh
    gh = github3.login(Github.user_name, password=Github.user_passwd)
    # if not has_commit_today():
    if True:
        fake_commit()


if __name__ == '__main__':
    main()
