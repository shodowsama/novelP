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

# github合併後本地操作(刪除分支)
git switch main
git pull
git branch -d backend
```

## 虛擬環境下pip install flask產生錯誤ModuleNotFoundError: No module named 'pip._internal'

```bash
python -m ensurepip
python -m pip install --upgrade pip
pip install flask
```

## 將資料庫中的url進行拆分以作為小說ID

```sql
alter table novels add book_id varchar(256);
update novels set book_id = substring_index(substring_index(book_menu_url,'book/',-1),'/',1);
```

## 依賴安裝

### 1. requirements

```bash
# 寫入
pip freeze > requirements.txt
# 安裝
pip install -r requirements.txt
```

### 2. toml (pip只會刪除直接依賴，間接依賴無法刪除)
手動新增檔案pyproject.toml，手動寫入。

```bash
# 安裝
pip install -e .
```

### 3. 使用uv安裝依賴和搭建虛擬環境(poetry也可)

```bash
# 創建
uv add flask
# 安裝
vu sync
```

### 4. request.form.get 抓取name屬性