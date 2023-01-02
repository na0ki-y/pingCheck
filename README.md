# pingCheck
# OverView　"pingCheck"

"pingCheck"は在室確認をWEBブラウザでどこからでも確認することができます。
登録は、ユーザ名と持っている端末の固有番号(MACアドレス)で行います。部屋の中のネット環境を通して在室が自動にチャックされWEB上でどこからでも確認できます。
[Go to app](https://na0ki-y-pingcheck-serverapp-k6hc0q.streamlit.app)
から確認することができます。


# DEMO
## CheckNow
![screenshot](/readme_image/readme_images.png)

## CheckLog

## Register


# Installation :balloon:
WEB表示は`python(stremlit)`で実装されています。
以下の通り、`pipenv`で環境構築後、ローカル環境で実行できます。

# Features
ネットワーク内で動かすチェッカーがデバイスをチェック（`ping/arp`)することで自動で、ユーザが在室しているか判定します。その結果を、`firebese`を通してWEBブラウザでどかからでも確認することができます。

機能は、現在の表示とログの確認、ユーザ登録です。

```bash
git clone git@github.com:na0ki-y/pingChecker.git
cd pingChecker
pipenv install
cd ./server
streamlit run app.py
```

`ping`による在室のチェックは`python`で実装されています。
以下の通り実行することで、ローカル環境で実行できます。
```bash
cd cd ./demon_checker
python py_checker.py
```


# Author
na_0ki