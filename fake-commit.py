#! /usr/bin/python
# -*- coding: utf-8 -*-

import github3
import time
import datetime

gh = None


class Github:
    user_name = "<user-name>"
    user_passwd = "<password>"
    fake_repo_name = "fake-commit-log"


def get_github_date():
    us_time = datetime.datetime.utcnow()
    # print us_time
    return str(us_time.date())


def has_commit_today():
    date = get_github_date()
    for repo in github3.iter_user_repos(Github.user_name):
        # print repo.pushed_at, repo.name
        if date in str(repo.pushed_at):
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
    t = get_github_date() + "-" + str(datetime.datetime.utcnow().time())[:5]

    path = "log/%s" % t
    msg = "hasnt commit at %s" % t
    content = t
    repo.create_file(path, msg, content)


def main():
    global gh
    gh = github3.login(Github.user_name, password=Github.user_passwd)
    if not has_commit_today():
        fake_commit()


if __name__ == '__main__':
    main()
