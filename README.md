# 112554016_paper-api
聊天系統 API

# 系統需求

python 3.9.x

# Quickstart

```
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# 離開 env
deactivate

# 使用單一應用程式設定一個新項目
django-admin startproject tutorial .
cd tutorial
django-admin startapp quickstart

# 同步資料庫
python manage.py migrate

# 建立初始 admin
python manage.py createsuperuser --username admin --email bird23074035@gmail.com # 0000


```

# Git template：(option)

```
git config --global commit.template .gitmessage.txt
```