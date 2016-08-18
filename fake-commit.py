#! /usr/bin/python
# -*- coding: utf-8 -*-

import github3
import time
import datetime
import random

gh = None


class Config:
    user_name = "<user_name>"
    user_passwd = "<user_passwd>"
    fake_repo_name = "fake-commit-log"


def get_github_date():
    us_time = datetime.datetime.utcnow()
    # print us_time
    return str(us_time.date())


def has_commit_today():
    date = get_github_date()
    try:
        repos = github3.iter_user_repos(Config.user_name)
    except Exception, e:
        raise e

    for repo in repos:
        # print repo.pushed_at, repo.name
        if date in str(repo.pushed_at):
            return True
    return False


def get_fake_repo():
    global gh
    try:
        repo = gh.repository(Config.user_name, Config.fake_repo_name)
    except Exception, e:
        raise e

    if repo:
        return repo
    else:
        try:
            new_repo = gh.create_repo(Config.fake_repo_name)
        except Exception, e:
            raise e
        return new_repo


def fake_commit():
    repo = get_fake_repo()
    if repo is None:
        print 'Repo Is None'
    else:
        print repo
    timestamp = get_github_date() + "-" + str(datetime.datetime.utcnow().time(
    ))[:5]

    path = "log/%s" % timestamp
    msg = "hasnt commit at %s" % timestamp
    content = timestamp
    try:
        repo.create_file(path, msg, content)
    except Exception, e:
        raise e
    print 'Fake Push is OK'


def main():
    global gh
    gh = github3.login(Config.user_name, password=Config.user_passwd)
    print 'Name : {}'.format(Config.user_name)
    if not has_commit_today():
        print 'hasnt push today ... '
        for x in xrange(random.randint(2, 10)):
            fake_commit()
    else:
        print 'You has pushed today ...'


if __name__ == '__main__':
    main()
