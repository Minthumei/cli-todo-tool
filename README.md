# 🗒️ CLI Todo Tool

シンプルで使いやすいコマンドラインのToDoツールです。タスクをJSONファイルで管理します。

## 🚀 使い方

```bash
# タスクを追加
python todo.py add 買い物に行く

# 一覧表示
python todo.py list

# タスクを完了にする
python todo.py done 1

# タスクを削除する
python todo.py delete 1

# ヘルプを表示
python todo.py help
```

## 📋 実行例

```
$ python todo.py add GitHubにプッシュする
✅ Task added: [1] GitHubにプッシュする

$ python todo.py add コードレビューをする
✅ Task added: [2] コードレビューをする

$ python todo.py list

📋 Your Todo List:
----------------------------------------
  ⬜ [1] GitHubにプッシュする
  ⬜ [2] コードレビューをする
----------------------------------------
  0/2 completed

$ python todo.py done 1
🎉 Completed: [1] GitHubにプッシュする

$ python todo.py list

📋 Your Todo List:
----------------------------------------
  ✅ [1] GitHubにプッシュする
  ⬜ [2] コードレビューをする
----------------------------------------
  1/2 completed
```

## 📁 データ保存

タスクは `todos.json` に自動保存されます。

## 🛠️ 動作環境

- Python 3.6+
- 追加ライブラリ不要（標準ライブラリのみ）
