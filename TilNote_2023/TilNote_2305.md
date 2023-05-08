# 概要
2023年5月に学習した内容の記録
WikiとしてまとめたものはNotionにて記録
https://www.notion.so/fusassy/Wiki-dc0c835d2009437bacb3b15429d1c920?pvs=4

# 230508
### 【HowTo】コマンドプロンプトの基礎コマンド
cd:ディレクトリを移動する
ls:ディレクトリ内に存在するディレクトリやファイルの一覧を確認する
mkdir:新しいディレクトリを作成する
echo:新規ファイルを作成する
rm:ファイルを削除する
mv:ファイルやディレクトリの名前を変更したり移動する
cp:ファイルをコピーする

※参考：https://296.co.jp/article/352315201909081628

### 【TroubleShooting】VSCodeのターミナルで、Ubuntu22.04からgit cloneをすると、「Could not resolve host: github.com」と表示
##### 方法_1

```
sudo service network-manager restart
```

上記で実行し、network-managerを再起動。

##### 方法_2
DNSサーバーを確認し、GoogleのDNSサーバーを使用するためのものを設定。以下を実行する。

```
sudo vi /etc/resolv.conf
```

以下の行を追加する。
```
nameserver 8.8.8.8
```

※この画面での編集手順は以下の通り

1. ターミナルで `sudo vi /etc/resolv.conf` を実行してください。
2. `i` キーを押して、編集モードに切り替えてください。
3. `nameserver 8.8.8.8` を追加してください。
4. `Esc` キーを押して、コマンドモードに切り替えてください。
5. `:wq` と入力して、保存して終了してください。

以上の手順で `sudo vi /etc/resolv.conf` を打って、`nameserver 8.8.8.8`を追加して保存することができます。
注視する際には、:qaと打って、Enterを押下。

##### 方法_3
プロキシ設定を確認。
会社や学校のネットワークを使用している場合は、プロキシ設定が正しく行われているか確認。プロキシ設定が必要な場合は、以下のコマンドを使用して設定。

```
git config --global http.proxy <http://プロキシサーバー>:ポート番号
```

プロキシサーバーとポート番号は、お使いの環境に合わせて設定してください。
