# External Secrets Webhook の動作確認

このプロジェクトは、KubernetesのExternal Secrets Operatorを使用してWebhook経由でシークレットを取得するデモ環境を構築するための手順を提供します。
FlaskサーバーがWebhookとして動作し、Kubernetesクラスター内でシークレットを提供します。

## 前提条件
ローカル環境で動作確認するには以下のツールが必要です。
インストールされていない場合は、以下のリンクからインストールしてください。

- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [Helm](https://helm.sh/ja/docs/intro/install/)

## セットアップ手順
### 1. Minikubeクラスターの起動
Minikubeクラスターを起動します。

```bash
minikube start
```

### 2. External Secrets Operatorのインストール
External Secrets OperatorをHelmを使用してインストールします。

```bash
helm repo add external-secrets https://charts.external-secrets.io
helm repo update
helm install external-secrets external-secrets/external-secrets --version 0.9.18
```

### 3. Flaskサーバーのセットアップ
MinikubeのDocker環境を使用してDockerイメージをビルドします。
```bash
eval $(minikube -p minikube docker-env)
docker build -t server:latest ./server
```

### 4. Kubernetesのリソースをデプロイ
KubernetesのDeployment、Secret Store、およびExternal Secretをデプロイします。

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/secret-store.yaml
kubectl apply -f k8s/external-secret.yaml
```

## 動作確認
### podの確認
```bash
kubectl get pods
```

### Flaskサーバーログの確認
```
kubectl logs <server-pod-name>
```

### ネットワークの状態確認
デバッグ用コンテナを起動し、ネットワークの状態を確認します。

```bash
# デバッグ用コンテナを起動
kubectl debug -it <external-secret-pod-name> --image=ubuntu

# デバッグ用コンテナ内でパッケージをインストール
apt-get update
apt-get install -y iproute2

# ssコマンドを実行してネットワークソケットの情報を表示
ss
```