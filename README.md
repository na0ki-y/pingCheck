# pingCheck
# OverView　"pingCheck"

"pingCheck"は在室確認をWEBブラウザでどこからでも確認することができます。
登録は、ユーザ名と持っている端末の固有番号(MACアドレス)で行います。部屋の中のネット環境を通して在室が自動にチャックされWEB上でどこからでも確認できます。
[Go to app](https://na0ki-y-pingcheck-serverapp-k6hc0q.streamlit.app)
から確認することができます。


# DEMO
## CheckNow
![screenshot](/readme_images/sec_check_now.png)

## CheckLog

## Register


# Features
ネットワーク内で動かすチェッカーがデバイスをチェック（`ping/arp`)することで自動で、ユーザが在室しているか判定します。その結果を、`firebese`を通してWEBブラウザでどかからでも確認することができます。

# Installation :balloon:
環境設定には`pipenv`を使用します。
Cherckerは`python`で`shell`を呼び出すことで実装されています。ローカルで実行します。
WEB表示は`python(stremlit)`で実装されています。ローカルまたは、`streamlit cloud`で実行します。

## Cehcker local $\times$ WEBserver local
`python setup.py both_demon_and_web`でCehcker とWEBをローカルで実行します。
```bash
git clone git@github.com:na0ki-y/pingChecker.git
python setup.py both_demon_and_web
```


## Cehcker local $\times$ WEBserver Cloud
`python setup.py only_demon`でCehckerをローカルで実行します。
WEBserverの`Streamlit Cloud`の設定は、次を参考に実行します。Main fileは`server/app.py`とし、secretsの設定が必要です。
[doc:streamlit-cloud:get-started](https://docs.streamlit.io/streamlit-cloud/get-started)
[doc:streamlit-cloud:secrets-management](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management)\

[Go to app](https://na0ki-y-pingcheck-serverapp-k6hc0q.streamlit.app)は Cehcker local $\times$ WEBserver Cloud　で実行されています。


```bash
git clone git@github.com:na0ki-y/pingChecker.git
python setup.py only_demon
```

## 実装
## Checker
`ping`による在室のチェックは`python`で実装されています。
以下の通り実行することで、ローカル環境で実行できます。
```bash
cd cd ./demon_checker
python py_checker.py
```
## WEBserber
```bash
git clone git@github.com:na0ki-y/pingChecker.git
cd pingChecker
pipenv install
cd ./server
streamlit run app.py
```
# Author
na_0ki