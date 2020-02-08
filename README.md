# auto_tin_manipulater
## ヘッドレスブラウザ
Chrome WEBdriverの公式ページは[こちら](http://chromedriver.chromium.org/getting-started)  
※以下、これを参考にして書き進める。

[Chrome driverのダウンロード](https://sites.google.com/a/chromium.org/chromedriver/downloads)


## 環境準備
### selenium
`pip install selenium`
```
with webdriver.Chrome() as driver:
    
```
## 謎単語/問題
* Chromium
* driverオブジェクト内には何があるんだろう？
* ページの遷移が完了したか確認したい
    ポーリング時間の指定？
    webdriverwaitが使えそう
    https://www.soudegesu.com/post/python/selenium-wait-element/
* Chromeを事前にログインした状態で操作できないものか
* driverのChrome関数やFirefox関数はexecutable_pathが明示的には不要？
## 学び
### selenium
以前はPhantomJSという物が使われていたが、開発がされなくなってしまい、
現在では PhantomJSの開発者でさえ他の物を使うように提言している。
#### ユースケースは？
主にテストで実施される。
##### アホやん…でも好き
* F5アタック
https://a-zumi.net/python-selenium-f5-repeat/
* Brute Forceアタック
https://blog.rinatussenov.com/brute-forcing-enterprise-with-python-selenium-and-phantomjs-4cb26b08bf1a

### assert文
`assert 'yahoo' in ['yahoo', 'google', 'amazon']`

### seleniumの使用はサイト側に検知される
https://stackoverflow.com/questions/33225947/can-a-website-detect-when-you-are-using-selenium-with-chromedriver

## 参考になったサイト
* http://magazine.a-n-t.jp/2018/11/selenium/
### みかくにん
* https://qiita.com/derodero24/items/9e9567790bde9e4b9d0c
* https://qiita.com/skimhiro/items/b49be0852e1892f7dbc0
    VXFD??興味深いね
* https://hacknote.jp/archives/48685/
    細かいオプションが載ってそう？
* https://s51517765.hatenadiary.jp/entry/2018/04/21/124342
    結構多岐にわたる動作をしている。
    firefoxだが、until関数で処理を同期的に実行もやっているぽい
* https://qiita.com/memakura/items/20a02161fa7e18d8a693
    多分これが一番詳細に記載されている。
    良記事！

# selenium Gridとは
それぞれのiPhoneやWindows、Linuxなどの環境にて
OSごとのテストを実施してくれる。
パラレルなので手軽かつ、高速なテスト手法である。
https://selenium.dev/documentation/en/grid/components_of_a_grid/


