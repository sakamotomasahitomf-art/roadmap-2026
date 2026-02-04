# バックエンド学習スターター（FastAPI）

このリポジトリは、**学習用の最小構成**で、FastAPI を使ったバックエンド開発の土台です。

## できること（最小）
- `/health` : ヘルスチェック API（200 OK を返す）
- `/api/v1/tasks` : タスクの CRUD（メモリ保存版）
- Lint（ruff）とテスト（pytest）を GitHub Actions で自動実行

## セットアップ
```bash
# 1) 仮想環境作成（任意: venv）
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\\Scripts\\activate

# 2) 依存インストール
pip install -U pip
pip install -r requirements.txt

# 3) 開発起動（ホットリロード）
uvicorn app.main:app --reload
# → http://127.0.0.1:8000/docs でSwaggerを確認
```

## テスト & Lint
```bash
ruff check .
pytest -q
```

## プロジェクト構成
```
app/
  main.py            # FastAPI エントリポイント
  models.py          # pydantic モデル
  routers.py         # ルータ（エンドポイント定義）
.github/
  workflows/ci.yml   # CI（ruff + pytest）
  ISSUE_TEMPLATE/
    issue_template.md
requirements.txt
pytest.ini
README.md
```

## よくあるエラーと対処
- `Address already in use`: 8000番ポートが使用中 → 別プロセスを終了 or `--port 8001` などに変更
- `ModuleNotFoundError`: 仮想環境が有効化されていない → `source .venv/bin/activate`

## 今後の拡張（学習ロードマップ）
- SQLite → PostgreSQL（SQLAlchemy / Alembic）
- JWT 認証 / RBAC
- Docker 化 / GitHub Actions で CI/CD
- 本番デプロイ（Render / Fly.io → AWS）
