# 先建立本地資料夾連上github之情況

```bash
# 初始化
git init 

# 追蹤文件
git add .

# 添加本地倉庫
git commit -m '初始化'

# 連接遠端倉庫(novel為遠端倉庫別名)
git remote add novel https://github.com/shodowsama/novelP.git

# 檢查地址
git remote -v

# 修改分支名
git branch -m main

# 將遠端倉庫拉入並合併
git pull --rebase novel main

# 推送至遠端倉庫( 使用-u默認)
git push -u novel main

# 創建分支
git switch -c backend

# 切換分支
git switch backend

# 推送分支
git push novel backend
```

## 虛擬環境下pip install flask產生錯誤ModuleNotFoundError: No module named 'pip._internal'

```bash
python -m ensurepip
python -m pip install --upgrade pip
pip install flask
```
