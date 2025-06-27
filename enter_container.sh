# 1. 現在のワークスペースフォルダのパスを取得
currentFolder="$(pwd)"

# 2. そのフォルダのラベルを持つコンテナのIDを検索
# Dockerの場合は --filter label=... で同様にフィルタ可能
containerId="$(docker ps --filter "label=devcontainer.local_folder=$currentFolder" --format "{{.ID}}")"

# 3. コンテナ内でzshを起動
docker exec -it "$containerId" zsh
