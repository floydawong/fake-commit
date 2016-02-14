#! /usr/bin/python
# -*- coding: utf-8 -*-

import github3
from datetime import *

gh = None


class Github:
    user_name = "<user-name>"
    user_passwd = "<password>"
    fake_repo_name = "fake-commit"


def get_github_time():
    utc = datetime.utcnow()
    return str(utc.date())


def has_commit_today():
    t = get_github_time()
    for repo in github3.iter_user_repos(Github.user_name):
        # print repo.updated_at, repo.pushed_at, repo.name
        if t in str(repo.pushed_at):
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
    # t = get_github_time()
    import random  # debug
    t = get_github_time() + "-" + str(random.randrange(1000))  # debug

    path = "log/%s" % t
    msg = "hasnt commit at %s" % t
    content = t
    repo.create_file(path, msg, content)


def main():
    global gh
    gh = github3.login(Github.user_name, password=Github.user_passwd)
    # if not has_commit_today():
    if True:  # debug
        fake_commit()


if __name__ == '__main__':
    main()
