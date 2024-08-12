# 112554016_paper-api
聊天系統 API

# start

```
python3 -m venv venv 
source venv/bin/activate # 可用 deactivate 關閉

pip install --upgrade pip
pip install .
uvicorn app.main:app --reload
```