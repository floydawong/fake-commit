# Fake Commit  

[中文](http://floyda.xyz/blog/2016/02/14/fake-commit/)  

![Contributions](https://raw.githubusercontent.com/KimDarren/git-faker/master/screenshots/after.png?token=AFIKQRYgdMW5jYxS_fH5fB_B3nHCTbO8ks5WfNVEwA%3D%3D)

> fake a commit to github, if you forgot.  
> you could deploy it on server, IDE plugins or system timer.  
> So you could be the best committer in the planet.  


## Environment  
- Python 2.7+
- [github3.py](https://github3py.readthedocs.org)
```shell
pip install github3.py
```

## Usage  
```bash
➜ git clone https://github.com/FloydaGithub/fake-commit.git
➜ cd fake-commit
➜ ./fake-commit.py
```

`Alert:` The first run is certainly an error. Because it will generate a `Config.py` file. Modify this file and run again.
