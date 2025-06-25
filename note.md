# 先建立本地資料夾連上github
## 1. 連線

```
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
# git branch -m main