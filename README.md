pythonのウェブフレームワークであるflaskを用いてpython練習
使用言語　Python, flaks, jQuery, html, 
2021/8/04

IDE: PyCharm
requirements.txt => install

<仕様>

AさんがBさんに1ビットコインを送ることを想定する。

使い方


AさんのウォレットにBさんのブロックチェーンアドレスを貼りつける.
いくつbitcoinを送るか指定し、(今回1ビットコイン）
sendボタンを押すと、Are you sure to send? と聞かれるので
okボタンを押す。

blockchain_server.pyで立ち上げた
'0.0.0.0:5000/transactions' を確認すると
length:1, 'transactions': [ 取引情報がはいる ] とAさん、Bさんのアドレス
及び、送ったビットコイン数（今回は１ビットコイン）入っているのが
確認できる。



'0.0.0.0:5000/chain' を確認すると、一番初めに作られたblock情報しか入っていない


理由はまだマイニングしていないからだ。
ブロックチェーンの取り引きの流れは
まず、transaction(取引情報：たとえばAさんがBさんに１ビットコイン送る等)
が transaction_pool たまっていき、
そのたまった取引情報が正しいを判断されたら（マイニング）
その塊（block)が連結されていく。
よってブロックチェーンとよぶ。

なので　'0.0.0.0:5000/mine' （マイニングurl)
と打ってやると、'0.0.0.0:5000/transactions' が空になっており、
'0.0.0.0:5000/chain' をリロード再確認すると、chain にblock情報が
格納されている。




(C) Copyright  Udemy course 現役シリコンバレーエンジニアが教えるPythonで始めるスクラッチからのブロックチェーン開発入門  All Rights Reserved.
