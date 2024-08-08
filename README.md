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

# 建立新的 app 應用
django-admin startproject tutorial1
python manage.py startapp snippets

# 當這一切完成後，我們需要更新我們的資料庫表。通常我們會建立一個資料庫遷移來執行此操作，但出於本教學的目的，讓我們刪除資料庫並重新開始。

rm -f db.sqlite3
rm -r snippets/migrations
python manage.py makemigrations snippets
python manage.py migrate

```

# Git template：(option)

```
git config --global commit.template .gitmessage.txt
```