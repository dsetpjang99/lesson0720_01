# GIT-DEMO


### Markdown 語法
- https://hackmd.io/@eMP9zQQ0Qt6I8Uqp2Vqy6w/SyiOheL5N/%2FBVqowKshRH246Q7UDyodFA?type=book

### 演練GIT相關指令

標題測試
=


重點指令
=
### 本地相關
- git init
    - 初始專案
- git add.
    - U/A/M/D (控管模式)
- git checkout .
    - 恢復修改 (反悔簡易恢復)
    - 任一個commit-object(sha-1編碼)/branch
- git commit -m "markdown註解"
    - 暫存區=>倉庫區
- git commit --amend
    - 合併上一次的commit
- git log / git status
- git checkout -b  <新增分支跟切換>
- git merge  <分支合併>
- git reset --hard HEAD(commit-object)
- git reflog
- git push
- git push -f

### 雲端相關
- github 申請新的專案倉庫網址(create new repository)
- git add remote origin https網址
- git remote -v
- git push -u origin master (首次將本地端資料傳送至遠端)
    - git push (第二次以後)
    - git push -f (force 強制將本地端版本傳送至遠端進行更新)

- 複製專案(首次於本地端建立專案目錄)
    - git clone https網址
- 遠端(雲端)同步專案到本地端(本地端已有專案，需要和由遠端將最新版本同步至本地端)
    - git pull